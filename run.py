import requests
import pandas as pd
from data import getTransactionData, getCurrentPrice
from processing import processing
from dataframe import createDataframe

userAddress = input("Please enter a Bitcoin address: ")
rawData = getTransactionData(userAddress)

if rawData:
    processedRawData = processing(rawData, userAddress)
    print(f"Retrieved and processed {len(processedRawData)} transactions.")
else:
    print("No transaction data retrieved.")

dataframe = createDataframe(processing(rawData, userAddress), getCurrentPrice(), userAddress)

def excelReport(dataframe, userAddress, filenamePrefix="address_statement"):
    dataframe.to_excel(f"{filenamePrefix}_{userAddress}.xlsx", index=False)

excelReport(dataframe, userAddress)