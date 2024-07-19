import pandas as pd
import os


def verify_data(tickers, input_dir):
    for ticker in tickers:
        print(f"Verifying data for {ticker}...")
        file_path = os.path.join(input_dir, f"{ticker}.csv")
        data = pd.read_csv(file_path)
        print(data.head())
