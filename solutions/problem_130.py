def profit_helper(prices, curr_index, curr_profit, buys_left, sells_left):

    if curr_index == len(prices) or not sells_left:
        # reached end of chronology or exhausted trades
        return curr_profit

    if buys_left == sells_left:
        # buy or wait
        return max(
            # buy
            profit_helper(prices, curr_index + 1, curr_profit - prices[curr_index],
                          buys_left - 1, sells_left),
            # wait
            profit_helper(prices, curr_index + 1, curr_profit,
                          buys_left, sells_left)
        )
    else:
        # sell or hold
        return max(
            # sell
            profit_helper(prices, curr_index + 1, curr_profit + prices[curr_index],
                          buys_left, sells_left - 1),
            # hold
            profit_helper(prices, curr_index + 1, curr_profit,
                          buys_left, sells_left)
        )


def get_max_profit(prices, k):
    return profit_helper(prices, 0, 0, k, k)


assert get_max_profit([5, 2, 4, 0, 1], 2) == 3
assert get_max_profit([5, 2, 4], 2) == 2
assert get_max_profit([5, 2, 4], 1) == 2
