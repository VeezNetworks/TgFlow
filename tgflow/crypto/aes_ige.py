from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def aes_ige_encrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    if len(data) % 16 != 0:
        raise ValueError("Data length must be multiple of 16")
    cipher = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
    iv1 = iv[:16]
    iv2 = iv[16:32]
    out = bytearray(len(data))
    for i in range(0, len(data), 16):
        block = data[i:i + 16]
        xored = bytes(a ^ b for a, b in zip(block, iv1))
        enc = cipher.update(xored)
        res = bytes(a ^ b for a, b in zip(enc, iv2))
        out[i:i + 16] = res
        iv1 = res
        iv2 = block
    return bytes(out)


def aes_ige_decrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    if len(data) % 16 != 0:
        raise ValueError("Data length must be multiple of 16")
    cipher = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
    iv1 = iv[:16]
    iv2 = iv[16:32]
    out = bytearray(len(data))
    for i in range(0, len(data), 16):
        block = data[i:i + 16]
        xored = bytes(a ^ b for a, b in zip(block, iv2))
        dec = cipher.update(xored)
        res = bytes(a ^ b for a, b in zip(dec, iv1))
        out[i:i + 16] = res
        iv1 = block
        iv2 = res
    return bytes(out)
