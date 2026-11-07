import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        # free_servers heap stores tuples of (weight, index)
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        
        # busy_servers heap stores tuples of (free_time, weight, index)
        busy_servers = []
        
        ans = []
        curr_time = 0
        
        for j, task_time in enumerate(tasks):
            curr_time = max(curr_time, j)
            
            # If no free servers are available, jump time to when the next server frees up
            if not free_servers and busy_servers[0][0] > curr_time:
                curr_time = busy_servers[0][0]
                
            # Release all servers that have finished their tasks by curr_time
            while busy_servers and busy_servers[0][0] <= curr_time:
                free_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
                
            # Assign the task to the best available server
            weight, index = heapq.heappop(free_servers)
            ans.append(index)
            
            # Push the server into busy_servers with its new release time
            heapq.heappush(busy_servers, (curr_time + task_time, weight, index))
            
        return ans