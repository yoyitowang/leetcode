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

#```
cap, n = map(int, input().split())

weights = list(map(int, input().split()))
prices = list(map(int, input().split()))
amounts = list(map(int, input().split()))

expanded_weights = []
expanded_prices = []

for i in range(n):
    weight = weights[i]
    price = prices[i]
    amount = amounts[i]
    k = 1
    while k <= amount:
        expanded_weights.append(k * weight)
        expanded_prices.append(k * price)
        amount -= k
        k *= 2
    if amount > 0:
        expanded_weights.append(amount * weight)
        expanded_prices.append(amount * price)
    

n = len(expanded_weights)
f = [0] * (cap+1)
# item -> knapsack
for i in range(n):
    weight = expanded_weights[i]
    price = expanded_prices[i]
    for c in range(cap, weight-1, -1):
        f[c] = max(f[c], f[c-weight] + price)
        
print(f[cap])
#```