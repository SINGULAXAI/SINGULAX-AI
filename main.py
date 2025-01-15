from flask import Flask, jsonify, request
from solana_connector import SolanaClient
from ai_module import AIModel
import os

app = Flask(__name__)

# Load environment variables
SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")
AI_MODEL_PATH = os.getenv("AI_MODEL_PATH", "models/singularx_model.pt")

# Initialize Solana client and AI model
solana_client = SolanaClient(SOLANA_RPC_URL)
ai_model = AIModel(AI_MODEL_PATH)


@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "SINGULAX AI is live!"})


@app.route("/wallet-info", methods=["POST"])
def wallet_info():
    data = request.json
    wallet_address = data.get("wallet_address")
    if not wallet_address:
        return jsonify({"error": "Wallet address is required"}), 400

    info = solana_client.get_wallet_info(wallet_address)
    return jsonify(info)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    user_input = data.get("input")
    if not user_input:
        return jsonify({"error": "Input data is required"}), 400

    prediction = ai_model.predict(user_input)
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(debug=True)
