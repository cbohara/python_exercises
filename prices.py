def solution(prices):
    min_value = min(prices)
    prices.reverse()
    min_value_index = prices.index(min_value)
    prices_slice = prices[:min_value_index+1]
    return max(prices_slice) - min_value


prices = [6, 0, -1, 10]
output = 11
assert solution(prices) == output

prices = [13, 10, 8, 4, 10]
output = 6
assert solution(prices) == output
