import pandas as pd
from datetime import datetime, timezone

def convert_to_dataframe(processed_data, live_price, user_address):
    
    total_received = sum(
    sum(float(value.split(" ")[0]) for value in tx["received_amount"].split(", ") if value) 
    if isinstance(tx["received_amount"], str) else sum(tx["received_amount"]) 
    for tx in processed_data
    )

    total_sent = sum(
    sum(float(value.split(" ")[0]) for value in tx["sent_amount"].split(", ") if value) 
    if isinstance(tx["sent_amount"], str) else sum(tx["sent_amount"]) 
    for tx in processed_data
    )

    confirmed_balance = total_received - total_sent

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    summary_data = {
        "Address Statement": [
            "Report for",
            "Generated at",
            "Total received",
            "Total sent",
            "Confirmed balance",
            "Live BTC/USD",
            "Confirmed transaction count"
        ],
        "": [
            user_address,
            timestamp,
            f"{total_received:.8f} BTC",
            f"{total_sent:.8f} BTC",
            f"{confirmed_balance:.8f} BTC",
            f"${live_price:,.2f}",
            f"{len(processed_data)}"
        ]
    }
    summary_df = pd.DataFrame(summary_data)
    transactions_df = pd.DataFrame(processed_data)

    return pd.concat([summary_df, transactions_df], axis=1).fillna("")