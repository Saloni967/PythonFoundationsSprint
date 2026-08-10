prices = [1245, 1210, 1235, 1190, 1275, 1310, 1280, 1350]

min_price = prices[0]
max_profit = 0

buy_day = 0
sell_day = 0
current_buy_day = 0

for i in range(1, len(prices)):

    # Find the lowest price
    if prices[i] < min_price:
        min_price = prices[i]
        current_buy_day = i

    # Calculate profit
    profit = prices[i] - min_price

    # Check if this is the best profit
    if profit > max_profit:
        max_profit = profit
        buy_day = current_buy_day
        sell_day = i

print("Maximum Profit: ₹", max_profit)
print("Buy Day:", buy_day + 1)
print("Buy Price: ₹", prices[buy_day])
print("Sell Day:", sell_day + 1)
print("Sell Price: ₹", prices[sell_day])