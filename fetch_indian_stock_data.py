from data_utils.indian_stock_data import IndianStockDataFetcher
import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description='Fetch historical data for Nifty 50 stocks')
    parser.add_argument('--start_date', type=str, default='2021-01-01',
                      help='Start date for historical data (YYYY-MM-DD)')
    parser.add_argument('--end_date', type=str, default=None,
                      help='End date for historical data (YYYY-MM-DD). Defaults to today.')
    parser.add_argument('--data_dir', type=str, default='data/price_history',
                      help='Directory to save the data')
    
    args = parser.parse_args()
    
    # Validate dates
    try:
        start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
        if args.end_date:
            end_date = datetime.strptime(args.end_date, '%Y-%m-%d')
        else:
            end_date = None
    except ValueError:
        print("Error: Dates must be in YYYY-MM-DD format")
        return
    
    # Initialize and run fetcher
    fetcher = IndianStockDataFetcher(data_dir=args.data_dir)
    fetcher.fetch_all_stocks(start_date=args.start_date, end_date=args.end_date)

if __name__ == "__main__":
    main() 