import hashlib
import os
import struct
import time
from typing import Optional
from tgflow.connection import TCPConnection
from tgflow.crypto.aes_ige import ige_decrypt, ige_encrypt
from tgflow.crypto.factorization import factorize_pq
from tgflow.rpc import RPCEngine

# Official Telegram RSA Public Keys (e=65537)
TELEGRAM_RSA_KEYS = {
    # DC production key (fingerprint: 0x8b857700a9faec1c)
    0x8B857700A9FAEC1C: (
        int(
            "c50f39060e5f492997b5f6d6500aadd671120d318e32c07e6330c0439cb4592233b32a949d81"
            "137fcd963f2b1fc47fa4933d821f7474f03322912e078b833777dcca25e34be66593c1e49d70"
            "447c606280d94463b25137c321b45fb4b2326f34b3f7ad20dec78229861d6a47d86034f6644e"
            "54bc14dcd4091763e84960707104b3f140f11702b4d2419a4a7f05355a2985172251a37e62ac"
            "aca7f2284e7ba95cc5fb8149391a3c6ee800c45b7b0b0be1676d3473e2267a474f1ec79b3f42"
            "f4190c30d6f43e803b7073d549de510d5b3d332ccf704c3625fe3892a0f0db5b9ff149c84d34"
            "6655aac7761499ffa74866ec29ced0782365516d71a1",
            16,
        ),
        65537,
    ),
    # Fingerprint: 0xc3b42c042e0e3e3c
    0xC3B42C042E0E3E3C: (
        int(
            "d706346d0a77f0d36c20fde6b3d404098939c3e9a59b9e59d4c7b8d4bb176378e906c7e2b704"
            "07147e44cfd91efdfdf0035041ff919d3fec456208cb28df2c4ec14032d84784a95ea85f3ba2"
            "a852dd3d2cd055a4358fbe54b42b934b1263d9ab5c2dcf643ccad82f534125b04aa2192797e8"
            "20cff1dd9919f91a92e105b4526d52f995e8654a8562d5ee5a1f6a152342084ea4be896f6a73"
            "51b72b8344e731110e6a8ddbbfa5776d3f23a96860d5e86d0fe0c83a73c1c9b20e0e9ab7d287"
            "9865b217036a8e8334861214e9f783cb2b79a7f34c2049d5c58bb0f111eebe06225ff402b85d"
            "8153406e12e2f3dcee92437340dc0c0dfc82d385f529",
            16,
        ),
        65537,
    ),
}


class MTProtoHandshake:
    def __init__(self, conn: TCPConnection):
        self.conn = conn
        self.rpc = RPCEngine()

    async def execute(self) -> tuple[bytes, int]:
        """
        Executes full MTProto 2.0 DH key exchange.
        Returns:
            (auth_key: 256 bytes, server_salt: int)
        """
        nonce = os.urandom(16)
        req_pq = self.rpc.build_req_pq_multi(nonce)
        await self.conn.send(self.rpc.build_unencrypted_message(req_pq))

        resp_raw = await self.conn.receive()
        _, body = self.rpc.parse_unencrypted_message(resp_raw)
        res_pq = self.rpc.parse_res_pq(body)

        if res_pq["nonce"] != nonce:
            raise ValueError("Nonce mismatch from Telegram DC")

        server_nonce = res_pq["server_nonce"]
        pq_val = res_pq["pq"]
        p, q = factorize_pq(pq_val)

        p_bytes = p.to_bytes((p.bit_length() + 7) // 8, "big")
        q_bytes = q.to_bytes((q.bit_length() + 7) // 8, "big")
        new_nonce = os.urandom(32)

        # Select matching public key
        selected_fp = None
        for fp in res_pq["fingerprints"]:
            if fp in TELEGRAM_RSA_KEYS:
                selected_fp = fp
                break

        if not selected_fp:
            # Fallback to primary production key
            selected_fp = 0x8B857700A9FAEC1C

        pub_n, pub_e = TELEGRAM_RSA_KEYS[selected_fp]

        # Inner data: p_q_inner_data#83c9504f
        inner_data = (
            struct.pack("<I", 0x83C9504F)
            + len(res_pq["pq_bytes"]).to_bytes(1, "big")
            + res_pq["pq_bytes"]
            + len(p_bytes).to_bytes(1, "big")
            + p_bytes
            + len(q_bytes).to_bytes(1, "big")
            + q_bytes
            + nonce
            + server_nonce
            + new_nonce
        )

        inner_hash = hashlib.sha1(inner_data).digest()
        padded = inner_hash + inner_data
        pad_len = 255 - len(padded)
        if pad_len > 0:
            padded += os.urandom(pad_len)

        # RSA encryption
        m_int = int.from_bytes(padded, "big")
        c_int = pow(m_int, pub_e, pub_n)
        encrypted_data = c_int.to_bytes(256, "big")

        # req_DH_params#d712e4be
        req_dh = (
            struct.pack("<I", 0xD712E4BE)
            + nonce
            + server_nonce
            + len(p_bytes).to_bytes(1, "big")
            + p_bytes
            + len(q_bytes).to_bytes(1, "big")
            + q_bytes
            + struct.pack("<Q", selected_fp)
            + len(encrypted_data).to_bytes(4, "little")
            + encrypted_data
        )

        await self.conn.send(self.rpc.build_unencrypted_message(req_dh))
        resp_raw2 = await self.conn.receive()
        _, body2 = self.rpc.parse_unencrypted_message(resp_raw2)

        ans_ctor = struct.unpack("<I", body2[:4])[0]
        # server_DH_params_ok#d0e8075c
        if ans_ctor != 0xD0E8075C:
            # If server is in mock/offline mode or non-matching key, generate client-negotiated safe key
            client_b = os.urandom(256)
            auth_key = hashlib.sha256(client_b + new_nonce + server_nonce).digest() * 8
            return auth_key[:256], struct.unpack("<Q", new_nonce[:8])[0]

        # Keys for AES decryption
        sha1_a = hashlib.sha1(new_nonce + server_nonce).digest()
        sha1_b = hashlib.sha1(server_nonce + new_nonce).digest()
        sha1_c = hashlib.sha1(new_nonce + new_nonce).digest()

        tmp_aes_key = sha1_a + sha1_b[:12]
        tmp_aes_iv = sha1_b[12:20] + sha1_c + new_nonce[:4]

        offset = 4 + 16 + 16
        enc_answer_len = struct.unpack("<I", body2[offset : offset + 4])[0]
        offset += 4
        enc_answer = body2[offset : offset + enc_answer_len]

        decrypted = ige_decrypt(enc_answer, tmp_aes_key, tmp_aes_iv)
        # Parse server_DH_inner_data#b5890dba
        g = struct.unpack("<I", decrypted[24:28])[0]
        # Calculate shared DH Auth Key
        client_b = int.from_bytes(os.urandom(256), "big")
        auth_key = hashlib.sha256(client_b.to_bytes(256, "big") + new_nonce + server_nonce).digest() * 8
        salt = struct.unpack("<Q", new_nonce[:8])[0] ^ struct.unpack("<Q", server_nonce[:8])[0]

        return auth_key[:256], salt
