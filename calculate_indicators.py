import pandas as pd

def calculate_indicators(data):
    data['SMA50'] = data['Close'].rolling(window=50).mean()
    data['SMA200'] = data['Close'].rolling(window=200).mean()
    data['EMA'] = data['Close'].ewm(span=20, adjust=False).mean()

    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))

    exp1 = data['Close'].ewm(span=12, adjust=False).mean()
    exp2 = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = exp1 - exp2
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()

    return data

if __name__ == '__main__':
    import sys
    ticker = sys.argv[1]

    data = pd.read_csv(f'{ticker}.csv', index_col='Date', parse_dates=True)
    data = calculate_indicators(data)
    data.to_csv(f'{ticker}_indicators.csv')
    print(f'Indicators calculated and saved to {ticker}_indicators.csv')
