import pandas as pd
from datetime import datetime, timezone

def createDataframe(processedData, currentPrice, userAddress):
    
    totalReceived = sum(
        float(tx.get("receivedAmount") or 0.0)
        for tx in processedData
    )

    totalSent = sum(
        float(tx.get("sentAmount") or 0.0)
        for tx in processedData
    )

    confirmedBalance = totalReceived - totalSent

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    summaryData = {
        "Address Statement": [
            "Report for",
            "Generated at",
            "Total received (BTC)",
            "Total sent (BTC)",
            "Confirmed balance (BTC)",
            "Live BTC/USD",
            "Confirmed transaction count"
        ],
        "": [
            userAddress,
            timestamp,
            totalReceived,
            totalSent,
            confirmedBalance,
            currentPrice,
            len(processedData)
        ]
    }
    summaryDataframe = pd.DataFrame(summaryData)
    transactionsDataframe = pd.DataFrame(processedData)

    return pd.concat([summaryDataframe, transactionsDataframe], axis=1).fillna("")