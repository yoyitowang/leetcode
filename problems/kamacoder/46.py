# zero-one knapsnak
n, bagweight = map(int, input().split())

weight = list(map(int, input().split()))
value = list(map(int, input().split()))

f = [[0 for _ in range(bagweight+1)] for _ in range(n+1)] 

# bag
# f[i][c] = max(f[i-1][c], f[i-1][c-w[i-1]] + v[i-1])
for i in range(n):
    for c in range(bagweight+1):
        if weight[i] > c:
            # f[i][c] = f[i-1][c]
            f[i+1][c] = f[i][c]
        else:
            # f[i][c] = max(f[i-1][c], f[i-1][c-weight[i-1]]+value[i-1])
            f[i+1][c] = max(f[i][c], f[i][c-weight[i]]+value[i])
print(f[n][bagweight])