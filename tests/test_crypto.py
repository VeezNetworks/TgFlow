import os
import unittest
from tgflow.crypto.aes_ige import aes_ige_encrypt, aes_ige_decrypt
from tgflow.crypto.factorization import factorize
from tgflow.crypto.obfuscated2 import Obfuscated2
from tgflow.crypto.diffie_hellman import derive_keys, compute_auth_key_id, create_auth_key


class TestCrypto(unittest.TestCase):
    def test_aes_ige_roundtrip(self) -> None:
        key = os.urandom(32)
        iv = os.urandom(32)
        plain = b"TelegramMTProto2.0SecurityBlock!" * 4
        cipher = aes_ige_encrypt(plain, key, iv)
        recovered = aes_ige_decrypt(cipher, key, iv)
        self.assertEqual(recovered, plain)

    def test_factorize(self) -> None:
        p1 = 1000000007
        p2 = 1000000009
        p, q = factorize(p1 * p2)
        self.assertEqual(p, p1)
        self.assertEqual(q, p2)

    def test_obfuscated2_handshake(self) -> None:
        obf = Obfuscated2()
        self.assertEqual(len(obf.header), 64)
        msg = b"PING"
        enc = obf.encrypt(msg)
        self.assertEqual(len(enc), len(msg))

    def test_kdf(self) -> None:
        ak = os.urandom(256)
        mk = os.urandom(16)
        k, iv = derive_keys(ak, mk, to_server=True)
        self.assertEqual(len(k), 32)
        self.assertEqual(len(iv), 32)

    def test_auth_key_id(self) -> None:
        ak = os.urandom(256)
        kid = compute_auth_key_id(ak)
        self.assertIsInstance(kid, int)


if __name__ == "__main__":
    unittest.main()
