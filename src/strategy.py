import pandas as pd
import os


def generate_signals(tickers, input_dir, output_dir):
    for ticker in tickers:
        print(f"Generating signals for {ticker}...")
        input_file = os.path.join(input_dir, f"{ticker}_preprocessed.csv")
        output_file = os.path.join(output_dir, f"{ticker}_signals.csv")

        data = pd.read_csv(input_file, index_col='Date', parse_dates=True)

        # Debug: First few rows of data
        print(f"First few rows of data for {ticker}:")
        print(data.head(20))

        # Check for NaNs in moving averages
        print(f"Checking for NaNs in moving averages for {ticker}:")
        print(data[['Short_MA', 'Long_MA']].isna().sum())

        # Generate signals
        data['Signal'] = 0
        data.loc[data['Short_MA'] > data['Long_MA'], 'Signal'] = 1
        data['Position'] = data['Signal'].diff()

        # Debug: First few rows after generating signals
        print(f"First few rows of moving averages and signals for {ticker}:")
        print(data[['Short_MA', 'Long_MA', 'Signal', 'Position']].head(20))

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        data.to_csv(output_file)
        print(f"Signals for {ticker} saved to {output_file}")
