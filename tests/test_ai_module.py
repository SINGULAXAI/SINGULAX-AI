import unittest
from ai_module import AIModel


class TestAIModel(unittest.TestCase):
    def setUp(self):
        self.model = AIModel("models/singularx_model.pt")

    def test_predict(self):
        input_text = "What is Solana?"
        prediction = self.model.predict(input_text)
        self.assertIsInstance(prediction, str)
        self.assertGreater(len(prediction), 0)


if __name__ == "__main__":
    unittest.main()
