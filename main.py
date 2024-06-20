import subprocess
import sys

def main(ticker, start_date, end_date):
    subprocess.run(['python', 'download_data.py', ticker, start_date, end_date])
    subprocess.run(['python', 'calculate_indicators.py', ticker])
    subprocess.run(['python', 'recommendations.py', ticker])

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python main.py <TICKER> <START_DATE> <END_DATE>")
    else:
        ticker = sys.argv[1]
        start_date = sys.argv[2]
        end_date = sys.argv[3]
        main(ticker, start_date, end_date)
