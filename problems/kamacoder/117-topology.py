from collections import defaultdict, deque

class KahnTopologicalSort:
    def __init__(self, v):
        self.V = v
        self.graph = defaultdict(list)

    def add_graph(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        # count in-degree
        in_degree = [0] * self.V

        for vals in self.graph.values():
            for v in vals:
                in_degree[v] += 1
        # priority queue: store 0 in-degree node
        que = deque([])
        for i in range(self.V):
            if in_degree[i] == 0:
                que.append(i)

        res = []
        count = 0
        while que:
            vertex = que.popleft()
            res.append(vertex)
            count += 1

            for neighbor in self.graph[vertex]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    que.append(neighbor)

        if self.V != count:
            return [-1]

        return res


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    kts = KahnTopologicalSort(n)
    for u, v in edges:
        kts.add_graph(u, v)
    ans = kts.topological_sort()
    print(" ".join(map(str, ans)))
