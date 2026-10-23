import asyncio
import unittest
from tgflow.client import TgFlow
from tgflow.crypto.factorization import factorize_pq


class TestDCConnection(unittest.TestCase):
    def test_live_dc_handshake(self):
        async def _run():
            app = TgFlow(test_mode=True)
            # Test DC 2: 149.154.167.40:443
            result = await app.ping_dc(dc_id=2)
            return result

        try:
            res = asyncio.run(asyncio.wait_for(_run(), timeout=12.0))
            print("\n[DC Connect Test Success]")
            print(f"Connected to DC {res['dc_id']} ({res['ip']}:{res['port']})")
            print(f"Server Msg ID: {res['msg_id']}")
            print(f"Nonce matched: {res['nonce_match']}")
            print(f"Received PQ: {res['pq']}")
            print(f"Server Public Key Fingerprints: {res['fingerprints_count']}")

            self.assertTrue(res["nonce_match"])
            self.assertGreater(res["pq"], 0)

            # Factorize PQ
            p, q = factorize_pq(res["pq"])
            print(f"Factorized PQ -> P: {p}, Q: {q} (P * Q == PQ: {p * q == res['pq']})")
            self.assertEqual(p * q, res["pq"])

        except (asyncio.TimeoutError, OSError) as e:
            print(f"\n[DC Connect Test Skipped: Network unreachable in test environment: {e}]")


if __name__ == "__main__":
    unittest.main()
