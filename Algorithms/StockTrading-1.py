prices1 = [7,1,5,3,6,4]

def MaxProfit(prices):
    min_price = 999999999
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
    
print(MaxProfit(prices1))