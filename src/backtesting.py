import pandas as pd
import os


def backtest_strategy(tickers, input_dir, output_dir, initial_capital=100000):
    for ticker in tickers:
        print(f"Backtesting strategy for {ticker}...")
        input_file = os.path.join(input_dir, f"{ticker}_signals.csv")
        output_file = os.path.join(output_dir, f"{ticker}_backtest.csv")

        data = pd.read_csv(input_file, index_col='Date', parse_dates=True)

        # Initialize portfolio
        data['Position'] = data['Position'].fillna(0).cumsum()
        data['Holdings'] = data['Position'] * data['Close']
        data['Cash'] = initial_capital - (data['Position'].diff().fillna(0) * data['Close']).cumsum()
        data['Total'] = data['Holdings'] + data['Cash']
        data['Returns'] = data['Total'].pct_change()

        print(f"Backtest results for {ticker}:")
        print(data[['Close', 'Position', 'Holdings', 'Cash', 'Total']].head(20))

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        data.to_csv(output_file)
        print(f"Backtest results for {ticker} saved to {output_file}")
