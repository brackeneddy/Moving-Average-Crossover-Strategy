import yfinance as yf
import os


def collect_data(tickers, start_date, end_date, output_dir):
    for ticker in tickers:
        print(f"Collecting data for {ticker}...")
        data = yf.download(ticker, start=start_date, end=end_date)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        file_path = os.path.join(output_dir, f"{ticker}.csv")
        data.to_csv(file_path)
        print(f"Data for {ticker} saved to {file_path}")
