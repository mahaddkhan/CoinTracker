import requests
import time

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/"

def fetch_coin(coin):
    coin = coin.lower()
    try:
        response = requests.get(COINGECKO_URL + coin)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError:
        print(f"Error fetching {coin}")
        return None