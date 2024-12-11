import requests
from data import get_transaction_data, get_price_log

def processing(raw_data, user_address):

    processed_data = []
    for transaction in raw_data:
        if "txid" in transaction and "status" in transaction:
            if "block_height" in transaction["status"] and "block_time" in transaction["status"]:
                txid = transaction["txid"]
                block_height = transaction["status"]["block_height"]
                block_time = transaction["status"]["block_time"]
                input_addresses, output_addresses, sent_amount, received_amount = [], [], [], []
                
                for vin in transaction.get("vin", []):
                    if "prevout" in vin and "scriptpubkey_address" in vin["prevout"]:
                        address = vin["prevout"]["scriptpubkey_address"]
                        input_addresses.append(address)

                        if address == user_address and "value" in vin["prevout"]:
                            sent_amount.append(vin["prevout"]["value"])

                for vout in transaction.get("vout", []):
                    if "scriptpubkey_address" in vout:
                        address = vout["scriptpubkey_address"]
                        output_addresses.append(address)
                        
                        if address == user_address and "value" in vout:
                            received_amount.append(vout["value"])

                price_data = get_price_log([block_time])
                btc_usd_price = price_data[0].get("BTC/USD", "N/A") if price_data else "N/A"
                
                processed_data.append({
                    "Transaction Hash": txid,
                    "Block Index": block_height,
                    "block_time": block_time,
                    "received_amount": "{:.8f}".format(received_amount[0] / 1e8) if received_amount else "",
                    "sent_amount": "{:.8f}".format(sent_amount[0] / 1e8) if sent_amount else "",
                    "BTC/USD": "{:,.2f}".format(btc_usd_price)
                })

    return processed_data