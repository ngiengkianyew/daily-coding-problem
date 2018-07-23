import sys


def get_stock_profit(prices):
    if not prices or len(prices) < 2:
        return

    min_price = prices[0]
    max_diff = -sys.maxsize
    for price in prices[1:]:
        if price - min_price > max_diff:
            max_diff = price - min_price
        if price < min_price:
            min_price = price

    return max_diff


assert get_stock_profit([9]) == None
assert get_stock_profit([9, 11, 8, 5, 7, 10]) == 5
assert get_stock_profit([1, 2, 3, 4, 5]) == 4
assert get_stock_profit([1, 1, 1, 1, 1]) == 0
assert get_stock_profit([1, 1, 1, 2, 1]) == 1
assert get_stock_profit([5, 4]) == -1
