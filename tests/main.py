import unittest
from app import app


class TestMainApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_status_endpoint(self):
        response = self.client.get("/status")
        self.assertEqual(response.status_code, 200)
        self.assertIn("SINGULAX AI is live!", response.get_json()["status"])

    def test_wallet_info_endpoint(self):
        response = self.client.post("/wallet-info", json={"wallet_address": "VALID_WALLET"})
        self.assertEqual(response.status_code, 200)

    def test_predict_endpoint(self):
        response = self.client.post("/predict", json={"input": "Tell me about Solana."})
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.get_json())


if __name__ == "__main__":
    unittest.main()
