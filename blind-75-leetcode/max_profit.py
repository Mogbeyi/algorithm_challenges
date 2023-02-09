def max_profit(prices):
    min_price = float('inf')
    profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = max(profit, price - min_price)

    return profit

print(max_profit([7,1,5,3,6,4]))
print(max_profit([7,6,4,3,1]))