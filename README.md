# Trading Bot

This project is an automated trading bot that uses technical indicators, namely Exponential Moving Average (EMA) and Simple Moving Average (SMA), to make trading decisions. The bot is coded in Python and uses the libraries `yfinance`, `pandas`, `ta`, and `datetime`.


## Features

- **Recovery of financial data** : The use of `yfinance` to get historical stock price data CAL.L
  (the action can be changed at the line 7).
- **Calculation of technical indicators** : Using Libraries `pandas`, and `ta` to calculate the EMA and SMA.
- **Generating trading signals** : Creation of buy and sell signals based on crosses of EMA and SMA.
- **Data logging** : The data is saved in the file bot1_{date}.csv
- **Execution of trades** : Implementation of trading logic based on generated signals.


## Goals

- **Improvement** : add better signals to make it more reliable.
- **Functional** : Create a working version with real money.


## Prerequisites

Before you begin, make sure you have installed the following libraries:

```bash
pip install yfinance pandas ta datetime
```
