# Unbounded knapsack problems

#```
cap, n = map(int, input().split())

weights = list(map(int, input().split()))
prices = list(map(int, input().split()))
amounts = list(map(int, input().split()))

for i in range(n):
    weight = weights[i]
    price = prices[i]
    amount = amounts[i]
    weights += [weight] * (amount-1)
    prices += [price] * (amount-1)

n = len(weights)
cache = {}
def dfs(i, c):
    if i < 0:
        return 0
    if (i, c) in cache:
        return cache[(i, c)]
    if weights[i] > c:
        ans = dfs(i-1, c)
    else:
        ans = max(dfs(i-1, c), dfs(i-1, c-weights[i]) + prices[i])
    cache[(i, c)] = ans
    return ans

print(dfs(n-1, cap))
#```