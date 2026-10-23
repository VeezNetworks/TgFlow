import os
import unittest
from tgflow.crypto.aes_ige import aes_ige_decrypt, aes_ige_encrypt
from tgflow.crypto.diffie_hellman import compute_auth_key_id, compute_msg_key, perform_dh_step
from tgflow.crypto.factorization import factorize_pq


class TestCrypto(unittest.TestCase):
    def test_aes_ige_roundtrip(self):
        key = os.urandom(32)
        iv = os.urandom(32)
        plaintext = b"Telegram MTProto 2.0 AES-IGE Testing Block!!"
        padding = (16 - (len(plaintext) % 16)) % 16
        plaintext += b"\x00" * padding

        encrypted = aes_ige_encrypt(plaintext, key, iv)
        self.assertNotEqual(encrypted, plaintext)
        self.assertEqual(len(encrypted), len(plaintext))

        decrypted = aes_ige_decrypt(encrypted, key, iv)
        self.assertEqual(decrypted, plaintext)

    def test_factorize_pq(self):
        p_expected = 1000000007
        q_expected = 1000000009
        pq = p_expected * q_expected

        p, q = factorize_pq(pq)
        self.assertEqual(p * q, pq)
        self.assertTrue(p <= q)
        self.assertEqual(p, p_expected)
        self.assertEqual(q, q_expected)

    def test_diffie_hellman(self):
        g = 3
        b = 123456789
        p = 2147483647
        result = perform_dh_step(g, b, p)
        expected = pow(g, b, p)
        self.assertEqual(result, expected)

    def test_auth_key_id(self):
        auth_key = os.urandom(256)
        key_id = compute_auth_key_id(auth_key)
        self.assertIsInstance(key_id, int)
        self.assertGreater(key_id, 0)


if __name__ == "__main__":
    unittest.main()
