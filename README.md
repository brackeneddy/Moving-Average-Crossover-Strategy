# Moving Average Crossover Trading Strategy

This project implements and backtests a simple moving average crossover trading strategy.

## Project Structure

- `data/`: Directory to store data files.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and prototyping.
- `src/`: Source code for the project.
  - `data_collection.py`: Script for collecting historical price data.
  - `preprocessing.py`: Script for data preprocessing.
  - `strategy.py`: Script for implementing the trading strategy.
  - `backtesting.py`: Script for backtesting the strategy.
  - `visualization.py`: Script for visualizing the strategy's performance.
- `tests/`: Directory for unit tests.
  - `test_strategy.py`: Unit tests for the trading strategy.
- `.gitignore`: Git ignore file.
- `README.md`: Project overview and instructions.
- `requirements.txt`: Python dependencies.

## Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/trading-strategy.git
cd trading-strategy
pip install -r requirements.txt
