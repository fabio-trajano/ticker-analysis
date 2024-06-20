import pandas as pd
import matplotlib.pyplot as plt

def plot_indicators(data, ticker):
    plt.figure(figsize=(14, 7))

    plt.subplot(3, 1, 1)
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['SMA50'], label='50-Day SMA', alpha=0.7)
    plt.plot(data['SMA200'], label='200-Day SMA', alpha=0.7)
    plt.title(f'{ticker} Price and Moving Averages')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(data['RSI'], label='RSI', color='orange')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red')
    plt.axhline(30, linestyle='--', alpha=0.5, color='green')
    plt.title('Relative Strength Index (RSI)')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(data['MACD'], label='MACD', color='purple')
    plt.plot(data['Signal_Line'], label='Signal Line', color='blue', alpha=0.7)
    plt.title('MACD')
    plt.legend()

    plt.tight_layout()
    plt.show()

def make_recommendation(data):
    if data['Close'].iloc[-1] > data['SMA200'].iloc[-1] and data['RSI'].iloc[-1] < 70:
        return 'Buy'
    elif data['Close'].iloc[-1] < data['SMA200'].iloc[-1] or data['RSI'].iloc[-1] > 70:
        return 'Sell'
    else:
        return 'Hold'

if __name__ == '__main__':
    import sys
    ticker = sys.argv[1]

    data = pd.read_csv(f'{ticker}_indicators.csv', index_col='Date', parse_dates=True)
    plot_indicators(data, ticker)
    recommendation = make_recommendation(data)
    print(f'Recommendation for {ticker}: {recommendation}')
