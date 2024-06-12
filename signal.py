import yfinance as yf
import pandas as pd
import time
from datetime import datetime

# Paramètres du bot
symbol = "CAL.L"
sma_period = 20
ema_period = 20
rsi_period = 14
bollinger_period = 20

# Fonction pour obtenir les données historiques et calculer les indicateurs
def get_data_with_indicators(symbol):
    data = yf.download(symbol, period='1d', interval='1m')

    # Calculer la SMA
    data['SMA_20'] = data['Close'].rolling(window=sma_period).mean()

    # Calculer l'EMA
    data['EMA_20'] = data['Close'].ewm(span=ema_period, adjust=False).mean()

    # Calculer le RSI
    delta = data['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=rsi_period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=rsi_period).mean()
    RS = gain / loss
    data['RSI_14'] = 100 - (100 / (1 + RS))

    # Calculer les Bollinger Bands
    data['BB_upper'] = data['Close'].rolling(window=bollinger_period).mean() + 2 * data['Close'].rolling(window=bollinger_period).std()
    data['BB_lower'] = data['Close'].rolling(window=bollinger_period).mean() - 2 * data['Close'].rolling(window=bollinger_period).std()

    return data

# Fonction pour générer des signaux de trading
def generate_signals(data):
    latest_data = data.iloc[-1]

    signals = {
        'achat': False,
        'vente': False,
        'conserver': True
    }

    # Critères SMA et EMA
    if latest_data['Close'] > latest_data['EMA_20']:
        signals['achat'] = True
        signals['vente'] = False
    elif latest_data['Close'] < latest_data['EMA_20']:
        signals['achat'] = False
        signals['vente'] = True

    # Critères RSI
    if latest_data['RSI_14'] < 30:
        signals['achat'] = True
        signals['vente'] = False
    elif latest_data['RSI_14'] > 70:
        signals['achat'] = False
        signals['vente'] = True

    # Critères Bollinger Bands
    if latest_data['Close'] < latest_data['BB_lower']:
        signals['achat'] = True
        signals['vente'] = False
    elif latest_data['Close'] > latest_data['BB_upper']:
        signals['achat'] = False
        signals['vente'] = True

    return signals

# Fonction pour sauvegarder les données et signaux dans un fichier CSV
def save_to_csv(data, signals, filename):
    latest_data = data.iloc[-1].to_dict()
    latest_data['Signal'] = 'Acheter' if signals['achat'] else 'Vendre' if signals['vente'] else 'Conserver'
    latest_data['Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    df = pd.DataFrame([latest_data])
    df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)

# Fonction principale du bot
def trading_bot():
    filename = f"bot1_{datetime.now().strftime('%Y-%m-%d')}.csv"
    
    while True:
        data = get_data_with_indicators(symbol)
        signals = generate_signals(data)

        if signals['achat']:
            print(f"{datetime.now()}: Signal d'achat pour {symbol}")
        elif signals['vente']:
            print(f"{datetime.now()}: Signal de vente pour {symbol}")
        else:
            print(f"{datetime.now()}: Signal de conservation pour {symbol}")

        save_to_csv(data, signals, filename)
        time.sleep(60)  # Attendre une minute avant la prochaine vérification

if __name__ == "__main__":
    trading_bot()

# Github : https://github.com/Valouzzzz/Trading-bot
# avoir fait la commande : pip install ta pandas yfinance datetime
