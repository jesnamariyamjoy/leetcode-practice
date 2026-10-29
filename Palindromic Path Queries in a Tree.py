class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = max(1, (n).bit_length())
        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        size = [1] * n
        base = [0] * n          # root->node parity mask for the initial string
        chars = [1 << (ord(c) - 97) for c in s]

        # Iterative DFS (preorder keeps every subtree contiguous)
        order = []
        stack = [0]
        base[0] = chars[0]
        while stack:
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)
            for w in adj[u]:
                if w != parent[u]:
                    parent[w] = u
                    depth[w] = depth[u] + 1
                    base[w] = base[u] ^ chars[w]
                    stack.append(w)
        for u in reversed(order):
            if parent[u] != -1:
                size[parent[u]] += size[u]

        # Binary lifting for LCA
        up = [[0] * n for _ in range(LOG)]
        for i in range(n):
            up[0][i] = parent[i] if parent[i] != -1 else i
        for j in range(1, LOG):
            prev, cur = up[j - 1], up[j]
            for i in range(n):
                cur[i] = prev[prev[i]]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            j = 0
            while diff:
                if diff & 1:
                    a = up[j][a]
                diff >>= 1
                j += 1
            if a == b:
                return a
            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]
            return up[0][a]

        # Fenwick tree: range XOR update, point query
        bit = [0] * (n + 2)

        def add(i, x):
            i += 1
            while i <= n + 1:
                bit[i] ^= x
                i += i & -i

        def point(i):
            i += 1
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r

        def pref(u):
            return base[u] ^ point(tin[u])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new = 1 << (ord(parts[2]) - 97)
                delta = chars[u] ^ new
                if delta:
                    chars[u] = new
                    add(tin[u], delta)
                    add(tin[u] + size[u], delta)
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                mask = pref(u) ^ pref(v) ^ chars[l]
                ans.append(mask & (mask - 1) == 0)
        return ans