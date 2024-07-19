import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_performance(tickers, input_dir, output_dir):
    for ticker in tickers:
        print(f"Plotting performance for {ticker}...")
        file_path = os.path.join(input_dir, f"{ticker}_backtest.csv")
        data = pd.read_csv(file_path, index_col='Date', parse_dates=True)

        plt.figure(figsize=(14, 7))
        plt.plot(data['Total'], label='Total Portfolio Value')
        plt.title(f'Performance of {ticker}')
        plt.xlabel('Date')
        plt.ylabel('Portfolio Value')
        plt.legend()

        output_file = os.path.join(output_dir, f"{ticker}_performance.png")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        plt.savefig(output_file)
        print(f"Performance plot for {ticker} saved to {output_file}")
        plt.close()
