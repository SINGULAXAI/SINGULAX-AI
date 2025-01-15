from solana.rpc.api import Client

class SolanaClient:
    def __init__(self, rpc_url):
        self.client = Client(rpc_url)

    def get_wallet_info(self, wallet_address):
        try:
            response = self.client.get_balance(wallet_address)
            return {"address": wallet_address, "balance": response["result"]["value"]}
        except Exception as e:
            return {"error": str(e)}
