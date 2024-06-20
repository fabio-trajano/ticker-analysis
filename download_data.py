import yfinance as yf


def download_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data = data['Close']
    return data


if __name__ == '__main__':
    import sys

    ticker = sys.argv[1]
    start_date = sys.argv[2]
    end_date = sys.argv[3]

    data = download_data(ticker, start_date, end_date)
    data.to_csv(f'{ticker}.csv')
    print(f'Data for {ticker} downloaded and saved to {ticker}.csv')
