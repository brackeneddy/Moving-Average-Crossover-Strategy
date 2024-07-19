import pandas as pd
import os


def verify_preprocessed_data(tickers, data_dir):
    for ticker in tickers:
        print(f"Verifying preprocessed data for {ticker}...")
        file_path = os.path.join(data_dir, f"{ticker}_preprocessed.csv")
        data = pd.read_csv(file_path, index_col='Date', parse_dates=True)

        print(data.head())

        # Check if moving averages are calculated correctly
        print("Moving Averages Check:")
        print(data[['Short_MA', 'Long_MA']].describe())

        print("\n")
