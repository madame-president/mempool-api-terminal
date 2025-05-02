import requests

def getTransactionData(address):
    staticUrl = f"https://mempool.space/api/address/{address}/txs"
    rawData, seenTransactions = [], set()
    after_txid = None
    try:
        while True:
            queryUrl = requests.get(f"{staticUrl}?after_txid={after_txid}" if after_txid else staticUrl)
            if queryUrl.status_code != 200:
                return None
            paginatedTransactions = queryUrl.json()
            if not paginatedTransactions:
                break
            for tx in paginatedTransactions:
                if tx["txid"] not in seenTransactions:
                    seenTransactions.add(tx["txid"])
                    rawData.append(tx)
            after_txid = paginatedTransactions[-1]["txid"] if paginatedTransactions else None
        return rawData
    except requests.RequestException:
        return None

def getPriceLog(block_times, currency="USD"):
    priceLog = []
    staticUrl = "https://mempool.space/api/v1/historical-price"
    for block_time in block_times:
        try:
            queryUrl = requests.get(staticUrl, params={"currency": currency, "timestamp": block_time})
            price = queryUrl.json().get("prices", [{}])[0].get(currency)
            if price is not None:
                priceLog.append({"timestamp": block_time, f"BTC/{currency}": price})
        except requests.RequestException:
            continue
    return priceLog

def getCurrentPrice():
    try:
        return requests.get("https://mempool.space/api/v1/prices").json().get("USD")
    except requests.RequestException:
        return None
