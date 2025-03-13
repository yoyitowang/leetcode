class UnionFind:
    # 1. find: root of node
    # 2. join: 2 point into 1 set
    # 3. is same: check are they same root
    def __init__(self, size):
        self.parent = [i for i in range(size+1)] # [0,1,2,3,...]
        self.rank = [1] * (size+1)

    def find(self, x):
        """
        find root of x and compress
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        

    def union(self, x, y):
        """
        union x and y
        attach smaller tree under bigger tree
        If ranks are equal, choose one as the new root and increase its rank
        """
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def isConnected(self, x, y):
        """
        check if containing x and y have same rank
        """

        return self.find(x) == self.find(y)

n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    uf.union(a, b)

x, y = map(int, input().split())
print(1 if uf.isConnected(x, y) else 0)
