from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def aes_ige_encrypt(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    if len(plaintext) % 16 != 0:
        raise ValueError("Plaintext length must be a multiple of 16")

    cipher = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
    iv1 = iv[:16]
    iv2 = iv[16:32]
    out = bytearray(len(plaintext))

    for offset in range(0, len(plaintext), 16):
        block = plaintext[offset : offset + 16]
        xored = bytes(a ^ b for a, b in zip(block, iv1))
        encrypted = cipher.update(xored)
        cipher_block = bytes(a ^ b for a, b in zip(encrypted, iv2))

        out[offset : offset + 16] = cipher_block
        iv1 = cipher_block
        iv2 = block

    return bytes(out)


def aes_ige_decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    if len(ciphertext) % 16 != 0:
        raise ValueError("Ciphertext length must be a multiple of 16")

    cipher = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
    iv1 = iv[:16]
    iv2 = iv[16:32]
    out = bytearray(len(ciphertext))

    for offset in range(0, len(ciphertext), 16):
        block = ciphertext[offset : offset + 16]
        xored = bytes(a ^ b for a, b in zip(block, iv2))
        decrypted = cipher.update(xored)
        plain_block = bytes(a ^ b for a, b in zip(decrypted, iv1))

        out[offset : offset + 16] = plain_block
        iv1 = block
        iv2 = plain_block

    return bytes(out)
