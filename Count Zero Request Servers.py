from collections import defaultdict

class Solution(object):
    def countServers(self, n, logs, x, queries):
        # Sort logs by timestamp
        logs.sort(key=lambda l: l[1])
        
        # Attach original indices to queries and sort by query time
        indexed_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        ans = [0] * len(queries)
        server_counts = defaultdict(int)
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        for q_idx, q_time in indexed_queries:
            window_start = q_time - x
            window_end = q_time
            
            # Expand the window to include logs up to window_end
            while right < num_logs and logs[right][1] <= window_end:
                server_counts[logs[right][0]] += 1
                right += 1
                
            # Shrink the window from the left to exclude logs older than window_start
            while left < num_logs and logs[left][1] < window_start:
                server_counts[logs[left][0]] -= 1
                if server_counts[logs[left][0]] == 0:
                    del server_counts[logs[left][0]]
                left += 1
                
            # Servers with 0 requests = total servers - servers with at least 1 request
            ans[q_idx] = n - len(server_counts)
            
        return ans