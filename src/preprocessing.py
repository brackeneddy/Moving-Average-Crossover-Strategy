import pandas as pd
import os


def preprocess_data(tickers, input_dir, output_dir, short_window=20, long_window=50):
    for ticker in tickers:
        print(f"Preprocessing data for {ticker}...")
        input_file = os.path.join(input_dir, f"{ticker}.csv")
        output_file = os.path.join(output_dir, f"{ticker}_preprocessed.csv")

        data = pd.read_csv(input_file, index_col='Date', parse_dates=True)
        data['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
        data['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        data.to_csv(output_file)
        print(f"Preprocessed data for {ticker} saved to {output_file}")
