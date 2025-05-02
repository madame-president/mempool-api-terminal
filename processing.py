import requests
from data import getTransactionData, getPriceLog

def processing(rawData, userAddress):

    processedData = []
    for transaction in rawData:
        if "txid" in transaction and "status" in transaction:
            if "block_height" in transaction["status"] and "block_time" in transaction["status"]:
                txid = transaction["txid"]
                blockHeight = transaction["status"]["block_height"]
                blockTime = transaction["status"]["block_time"]
                inputs, outputs, sentAmount, receivedAmount = [], [], [], []
                
                for vin in transaction.get("vin", []):
                    if "prevout" in vin and "scriptpubkey_address" in vin["prevout"]:
                        address = vin["prevout"]["scriptpubkey_address"]
                        inputs.append(address)

                        if address == userAddress and "value" in vin["prevout"]:
                            sentAmount.append(vin["prevout"]["value"])

                for vout in transaction.get("vout", []):
                    if "scriptpubkey_address" in vout:
                        address = vout["scriptpubkey_address"]
                        outputs.append(address)
                        
                        if address == userAddress and "value" in vout:
                            receivedAmount.append(vout["value"])

                priceData = getPriceLog([blockTime])
                btcUsd = priceData[0].get("BTC/USD", "N/A") if priceData else "N/A"
                
                processedData.append({
                    "Transaction Hash": txid,
                    "Block Index": blockHeight,
                    "Block Time": blockTime,
                    "receivedAmount": sum(receivedAmount) / 1e8 if receivedAmount else None,
                    "sentAmount": sum(sentAmount) / 1e8 if sentAmount else None,
                    "BTC/USD": btcUsd
                })

    return processedData