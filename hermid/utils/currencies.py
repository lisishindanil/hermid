from mubble.client import AiohttpClient

client = AiohttpClient()


class Currency:
    def __init__(self, token: str) -> None:
        self.__link = f"https://v6.exchangerate-api.com/v6/{token}/latest/"

    async def get_currency(self, currency: str) -> dict:
        response = await client.request_json(self.__link + currency)
        if response["result"] == "error":
            return False

        return response["conversion_rates"]


class Cryptocurrency:
    def __init__(self, token: str) -> None:
        self.__link = f"https://rest.coinapi.io/jsonrpc/apikey-{token}"

    async def get_currency(self, crypto_currency: str):
        response = await client.request_json(
            url=self.__link,
            method="POST",
            data={
                "jsonrpc": "2.0",
                "method": f"v1/exchangerate/BTC",
                "params": [],
                "id": "my-tracking-id-001",
            },
        )
        return response
