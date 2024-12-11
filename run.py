import requests
import pandas as pd
from data import get_transaction_data, get_live_price
from processing import processing
from dataframe import convert_to_dataframe

user_address = input("Please enter a Bitcoin address: ")
raw_data = get_transaction_data(user_address)

if raw_data:
    processed_raw_data = processing(raw_data, user_address)
    print(f"Retrieved and processed {len(processed_raw_data)} transactions.")
else:
    print("No transaction data retrieved.")

df = convert_to_dataframe(processing(raw_data, user_address), get_live_price(), user_address)

def save_to_xlsx(df, user_address, filename_prefix="address_statement"):
    df.to_excel(f"{filename_prefix}_{user_address}.xlsx", index=False)

save_to_xlsx(df, user_address)