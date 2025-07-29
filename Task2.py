# Hardcoded stock prices
stock_prices = {
    'AAPL': 180,
    'TSLA': 250,
    'GOOG': 2800,
    'MSFT': 310
}

portfolio = {}
total_investment = 0

print("Available stocks:", ', '.join(stock_prices.keys()))
n = int(input("How many different stocks do you own? "))

for _ in range(n):
    stock = input("Enter stock symbol: ").upper()
    qty = int(input(f"Enter quantity of {stock}: "))
    if stock in stock_prices:
        investment = stock_prices[stock] * qty
        portfolio[stock] = (qty, investment)
        total_investment += investment
    else:
        print(f"{stock} not found in stock list.")

print("\n📊 Your Portfolio:")
for stock, (qty, invest) in portfolio.items():
    print(f"{stock}: {qty} shares → ₹{invest}")

print(f"\n💰 Total Investment Value: ₹{total_investment}")
