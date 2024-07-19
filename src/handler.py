import os
import pandas as pd
from data.preprocessing import DataLoader
from strategy import MovingAverageCrossoverStrategy
from backtesting import Backtester
import visualization as vis

def process_file(file_path, output_dir):
    # Load data
    data_loader = DataLoader(file_path)
    price_data = data_loader.load_data()

    # Initialize and run the strategy
    short_window = 40
    long_window = 100
    strategy = MovingAverageCrossoverStrategy(price_data, short_window, long_window)
    signals = strategy.generate_signals()

    # Backtest the strategy
    initial_capital = 100000.0
    backtester = Backtester(price_data, signals, initial_capital)
    backtest_results = backtester.run_backtest()

    # Extract the file name without extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Save signals and backtest results
    signals.to_csv(os.path.join(output_dir, 'signals', f'{file_name}_signals.csv'))
    backtest_results.to_csv(os.path.join(output_dir, 'backtest', f'{file_name}_backtest_results.csv'))

    # Visualization
    vis.plot_signals(price_data, signals, short_window, long_window, output_file=os.path.join(output_dir, 'plots', f'{file_name}_signals_plot.png'))
    vis.plot_backtest_results(backtest_results, output_file=os.path.join(output_dir, 'plots', f'{file_name}_backtest_results_plot.png'))

def main():
    raw_data_dir = 'data/raw'
    output_dir = 'data'
    os.makedirs(os.path.join(output_dir, 'signals'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'backtest'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'plots'), exist_ok=True)

    for file_name in os.listdir(raw_data_dir):
        if file_name.endswith('.csv'):
            file_path = os.path.join(raw_data_dir, file_name)
            process_file(file_path, output_dir)

if __name__ == "__main__":
    main()
