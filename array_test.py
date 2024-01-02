# 주식 시장에서 한번의 거래로 낼 수 있는 최대의 이득
# 입력
# [7,1,5,4,6,4]
# 출력
# 5

import sys


# 브루트 포스
def max_profit_bp(prices):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price


# 지점과 현재값과의 차이 계산
def max_profit(prices):
    profit = 0
    min_price = sys.maxsize
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit


q = max_profit([7, 1, 5, 4, 6, 4])
assert q == 5
print(q)
