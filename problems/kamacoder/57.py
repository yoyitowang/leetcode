# 57. 爬楼梯（第八期模拟笔试）
# 题目描述
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 

# 每次你可以爬至多m (1 <= m < n)个台阶。你有多少种不同的方法可以爬到楼顶呢？ 

# 注意：给定 n 是一个正整数。

# 输入描述
# 输入共一行，包含两个正整数，分别表示n, m
# 输出描述
# 输出一个整数，表示爬到楼顶的方法数。
# 输入示例
# 3 2
# 输出示例
# 3
# 提示信息
# 数据范围：
# 1 <= m < n <= 32;

# 当 m = 2，n = 3 时，n = 3 这表示一共有三个台阶，m = 2 代表你每次可以爬一个台阶或者两个台阶。

# 此时你有三种方法可以爬到楼顶。


# 1 阶 + 1 阶 + 1 阶段
# 1 阶 + 2 阶
# 2 阶 + 1 阶

# ```
cap, n = map(int, input().split())
f = [1] + [0] * cap

# f[i] = f[i-1] + f[i-2] + f[i-3] + ...
# f[1] = f[0]
# f[2] = f[1] + f[0]
# f[3] = f[2] + f[1] + f[0]
for i in range(1, cap+1):
    f[i] = sum(f[i-x] for x in range(1, n+1) if x <= i)
print(f[cap])
# ```

# ```
cap, n = map(int, input().split())

cache = {}
def dfs(i):
    if i == 0:
        return 1
    if i < 0:
        return 0
    if i in cache:
        return cache[i]
    total = sum(dfs(i-x) for x in range(1, n+1) if i>=x)
    cache[i] = total
    return total
    
print(dfs(cap))
# ```
