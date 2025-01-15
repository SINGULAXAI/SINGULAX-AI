import unittest
from solana_connector import SolanaClient


class TestSolanaClient(unittest.TestCase):
    def setUp(self):
        self.client = SolanaClient("https://api.devnet.solana.com")

    def test_get_wallet_info_valid(self):
        wallet_address = "VALID_WALLET_ADDRESS"
        response = self.client.get_wallet_info(wallet_address)
        self.assertIn("balance", response)

    def test_get_wallet_info_invalid(self):
        wallet_address = "INVALID_WALLET_ADDRESS"
        response = self.client.get_wallet_info(wallet_address)
        self.assertIn("error", response)


if __name__ == "__main__":
    unittest.main()
