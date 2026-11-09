import heapq
from sortedcontainers import SortedList

class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        available = SortedList(range(k))
        busy = []
        req_count = [0] * k
        
        for i in range(len(arrival)):
            arr_time = arrival[i]
            dur = load[i]
            
            # 1. Free up servers that have completed their tasks by the current arrival time
            while busy and busy[0][0] <= arr_time:
                _, s_id = heapq.heappop(busy)
                available.add(s_id)
                
            # If no servers are available, drop the request
            if not available:
                continue
                
            # 2. Find the first available server >= (i % k) using binary search
            target = i % k
            idx = available.bisect_left(target)
            
            # If no server >= target is available, wrap around to the beginning
            if idx == len(available):
                idx = 0
                
            server = available[idx]
            
            # 3. Assign the request to the chosen server
            available.pop(idx)
            heapq.heappush(busy, (arr_time + dur, server))
            req_count[server] += 1
            
        # Find the maximum number of requests handled by any server
        max_req = max(req_count) if req_count else 0
        
        # Return all servers that handled the maximum number of requests
        return [i for i, c in enumerate(req_count) if c == max_req]