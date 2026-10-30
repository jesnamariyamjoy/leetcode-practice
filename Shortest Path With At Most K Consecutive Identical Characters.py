import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        K = k + 1
        dist = [float('inf')] * (n * K)   # dist[node * K + run]
        dist[1] = 0                       # start at node 0 with run length 1
        best = [K] * n                    # smallest run already settled per node
        heap = [(0, 0, 1)]
        while heap:
            d, u, r = heapq.heappop(heap)
            if u == n - 1:
                return d
            if d > dist[u * K + r] or r >= best[u]:
                continue
            best[u] = r
            for v, w in adj[u]:
                nr = r + 1 if labels[v] == labels[u] else 1
                if nr <= k and d + w < dist[v * K + nr]:
                    dist[v * K + nr] = d + w
                    heapq.heappush(heap, (d + w, v, nr))
        return -1