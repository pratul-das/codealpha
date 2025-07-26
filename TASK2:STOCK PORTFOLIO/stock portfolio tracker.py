prices = {
    "AAPL": 188,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 125,
    "MSFT": 330
}

portfolio = {}
total = 0

while True:
    stock = input("Stock (or done): ").upper()
    if stock == "DONE":
        break
    if stock in prices:
        qty = int(input("Quantity: "))
        portfolio[stock] = qty
    else:
        print("Not found")

for stock in portfolio:
    value = prices[stock] * portfolio[stock]
    print(stock, ":", value)
    total += value

print("Total:", total)

# Save (optional)
save = input("Save to file? (y/n): ")
if save == "y":
    with open("portfolio.txt", "w") as f:
        for stock in portfolio:
            f.write(f"{stock},{portfolio[stock]},{prices[stock]},{portfolio[stock]*prices[stock]}\n")
        f.write(f"Total: {total}\n")