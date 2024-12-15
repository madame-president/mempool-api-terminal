import requests

def get_transaction_data(address):
    endpoint = f"https://mempool.space/api/address/{address}/txs"
    raw_data, seen_txids = [], set()
    after_txid = None
    try:
        while True:
            response = requests.get(f"{endpoint}?after_txid={after_txid}" if after_txid else endpoint)
            if response.status_code != 200:
                return None
            paginated_data = response.json()
            if not paginated_data:
                break
            for tx in paginated_data:
                if tx["txid"] not in seen_txids:
                    seen_txids.add(tx["txid"])
                    raw_data.append(tx)
            after_txid = paginated_data[-1]["txid"] if paginated_data else None
        return raw_data
    except requests.RequestException:
        return None

def get_price_log(block_times, currency="USD"):
    price_log = []
    endpoint = "https://mempool.space/api/v1/historical-price"
    for block_time in block_times:
        try:
            response = requests.get(endpoint, params={"currency": currency, "timestamp": block_time})
            price = response.json().get("prices", [{}])[0].get(currency)
            if price is not None:
                price_log.append({"timestamp": block_time, f"BTC/{currency}": price})
        except requests.RequestException:
            continue
    return price_log

def get_live_price():
    try:
        return requests.get("https://mempool.space/api/v1/prices").json().get("USD")
    except requests.RequestException:
        return None
