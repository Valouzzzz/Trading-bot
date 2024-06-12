import yfinance as yf
import pandas as pd
import time
from datetime import datetime

# Bot Settings
symbol = "CAL.L"
sma_period = 20
ema_period = 20
rsi_period = 14
bollinger_period = 20

# Function to obtain historical data and calculate indicators
def get_data_with_indicators(symbol):
    data = yf.download(symbol, period='1d', interval='1m')

    # Calculate the SMA
    data['SMA_20'] = data['Close'].rolling(window=sma_period).mean()

    # Calculate the EMA
    data['EMA_20'] = data['Close'].ewm(span=ema_period, adjust=False).mean()

    # Calculate the RSI
    delta = data['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=rsi_period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=rsi_period).mean()
    RS = gain / loss
    data['RSI_14'] = 100 - (100 / (1 + RS))

    # Calculate the Bollinger Bands
    data['BB_upper'] = data['Close'].rolling(window=bollinger_period).mean() + 2 * data['Close'].rolling(window=bollinger_period).std()
    data['BB_lower'] = data['Close'].rolling(window=bollinger_period).mean() - 2 * data['Close'].rolling(window=bollinger_period).std()

    return data

# Function for generating trading signals
def generate_signals(data):
    latest_data = data.iloc[-1]

    signals = {
        'buy': False,
        'sell': False,
        'hold': True
    }

    # Criteria SMA and EMA
    if latest_data['Close'] > latest_data['EMA_20']:
        signals['buy'] = True
        signals['sell'] = False
    elif latest_data['Close'] < latest_data['EMA_20']:
        signals['buy'] = False
        signals['sell'] = True

    # Criteria RSI
    if latest_data['RSI_14'] < 30:
        signals['buy'] = True
        signals['sell'] = False
    elif latest_data['RSI_14'] > 70:
        signals['buy'] = False
        signals['sell'] = True

    # Criteria Bollinger Bands
    if latest_data['Close'] < latest_data['BB_lower']:
        signals['buy'] = True
        signals['sell'] = False
    elif latest_data['Close'] > latest_data['BB_upper']:
        signals['buy'] = False
        signals['sell'] = True

    return signals

# Function to save data and signals in a CSV file
def save_to_csv(data, signals, filename):
    latest_data = data.iloc[-1].to_dict()
    latest_data['Signal'] = 'Buy' if signals['buy'] else 'Sell' if signals['sell'] else 'Hold'
    latest_data['Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    df = pd.DataFrame([latest_data])
    df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)

# Main function of the bot
def trading_bot():
    filename = f"bot1_{datetime.now().strftime('%Y-%m-%d')}.csv"
    
    while True:
        data = get_data_with_indicators(symbol)
        signals = generate_signals(data)

        if signals['buy']:
            print(f"{datetime.now()}: Buy signal for {symbol}")
        elif signals['sell']:
            print(f"{datetime.now()}: Sell signal for {symbol}")
        else:
            print(f"{datetime.now()}: Hold signal for {symbol}")

        save_to_csv(data, signals, filename)
        time.sleep(60)  # Wait one minute before the next check

if __name__ == "__main__":
    trading_bot()

# Github : https://github.com/Valouzzzz/Trading-bot
# have made the order : pip install ta pandas yfinance datetime
