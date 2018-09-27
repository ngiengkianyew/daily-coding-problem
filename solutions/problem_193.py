def get_max_profit(prices, fee, reserve=0, buyable=True):
    if not prices:
        return reserve

    price_offset = -prices[0] - fee if buyable else prices[0]
    return max(
        get_max_profit(prices[1:], fee, reserve, buyable),
        get_max_profit(prices[1:], fee, reserve + price_offset, not buyable)
    )



# Tests
assert get_max_profit([1, 3, 2, 8, 4, 10], 2) == 9
assert get_max_profit([1, 3, 2, 1, 4, 10], 2) == 7
