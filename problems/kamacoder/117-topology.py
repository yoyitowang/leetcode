    from collections import defaultdict, deque

    class KahnTopologicalSort:
        def __init__(self, v):
            self.V = v
            self.graph = defaultdict(list)

        def add_graph(self, u, v):
            self.graph[u].append(v)

        def topological_sort(self):
            in_degree = [0] * self.V
            # count each in_degree of vertex
            for vals in self.graph.values():
                for v in vals:
                    in_degree[v] += 1
            
            # add in_degree = 0 to queue
            que = deque([])
            for i, x in enumerate(in_degree):
                if x == 0:
                    que.append(i)
            
            res = []
            while que:
                vertex = que.popleft()
                res.append(vertex)
                
                for _next in self.graph[vertex]:
                    in_degree[_next] -= 1
                    if in_degree[_next] == 0:
                        que.append(_next)

            if len(res) != self.V:
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
