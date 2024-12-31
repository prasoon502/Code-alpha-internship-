import yfinance as yf
import pandas as pd
class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        if ticker in self.portfolio:
            self.portfolio[ticker]['shares'] += shares
        else:
            self.portfolio[ticker] = {'shares': shares, 'price': self.get_current_price(ticker)}

    def remove_stock(self, ticker, shares):
        if ticker in self.portfolio:
            if self.portfolio[ticker]['shares'] >= shares:
                self.portfolio[ticker]['shares'] -= shares
                if self.portfolio[ticker]['shares'] == 0:
                    del self.portfolio[ticker]
            else:
                print("You don't have enough shares to remove.")
        else:
            print("You don't own any shares of this stock.")

    def track_performance(self):
        total_value = 0
        for ticker, info in self.portfolio.items():
            current_price = self.get_current_price(ticker)
            total_value += current_price * info['shares']
            print(f"{ticker}: {info['shares']} shares, current price: ${current_price:.2f}, total value: ${current_price * info['shares']:.2f}")
        print(f"Total portfolio value: ${total_value:.2f}")

    def get_current_price(self, ticker):
        ticker_data = yf.Ticker(ticker)
        return ticker_data.info['regularMarketPrice']

def main():
    portfolio = StockPortfolio()
    while True:
        print("1. Add stock to portfolio")
        print("2. Remove stock from portfolio")
        print("3. Track portfolio performance")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            ticker = input("Enter the stock ticker: ")
            shares = int(input("Enter the number of shares: "))
            portfolio.add_stock(ticker, shares)
        elif choice == "2":
            ticker = input("Enter the stock ticker: ")
            shares = int(input("Enter the number of shares: "))
            portfolio.remove_stock(ticker, shares)
        elif choice == "3":
            portfolio.track_performance()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()