class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size+1)]
        self.rank = [1] * (size+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rX = self.find(x)
        rY = self.find(y)

        if rX != rY:
            if self.rank[rX] > self.rank[rY]:
                self.parent[rY] = rX
            elif self.rank[rX] < self.rank[rY]:
                self.parent[rX] = rY
            else:
                self.parent[rY] = rX
                self.rank[rX] += 1

    def isSame(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    # 輸入
    n = int(input())

    uf = UnionFind(n)
    for _ in range(n):
        x, y = map(int, input().split())
        if uf.isSame(x, y):
            print(x, y)
            exit()
        uf.union(x, y)
