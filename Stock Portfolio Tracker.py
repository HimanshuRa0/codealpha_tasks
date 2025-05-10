# stock_portfolio_tracker.py
import yfinance as yf

# Simple in-memory portfolio (dictionary)
portfolio = {}

def add_stock():
    ticker = input("Enter stock ticker (e.g. AAPL): ").upper()
    shares = int(input("Enter number of shares: "))
    portfolio[ticker] = portfolio.get(ticker, 0) + shares
    print(f"{shares} shares of {ticker} added.\n")

def remove_stock():
    ticker = input("Enter stock ticker to remove: ").upper()
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"{ticker} removed from portfolio.\n")
    else:
        print("Stock not found in portfolio.\n")

def view_portfolio():
    if not portfolio:
        print("Portfolio is empty.\n")
        return

    total_value = 0
    print("Current Portfolio:")
    print("{:<10} {:<10} {:<10} {:<10}".format("Ticker", "Shares", "Price", "Total Value"))

    for ticker, shares in portfolio.items():
        stock = yf.Ticker(ticker)
        try:
            price = stock.info['regularMarketPrice']
        except:
            price = 0.0
        value = price * shares
        total_value += value
        print("{:<10} {:<10} ${:<9.2f} ${:<10.2f}".format(ticker, shares, price, value))
    
    print(f"\nTotal Portfolio Value: ${total_value:.2f}\n")

def main():
    while True:
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_stock()
        elif choice == '2':
            remove_stock()
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
