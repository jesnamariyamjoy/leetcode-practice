class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        distance_val = 0
        
        for x in arr1:
            # We want to check if there is any y in arr2 such that x - d <= y <= x + d
            # Let's find the first element in arr2 that is >= x - d
            import bisect
            idx = bisect.bisect_left(arr2, x - d)
            
            # Check if this element or the previous element is within x + d
            found = False
            if idx < len(arr2) and arr2[idx] <= x + d:
                found = True
            if idx > 0 and arr2[idx - 1] >= x - d:
                found = True
                
            # If no element in arr2 falls in the range, it contributes to the distance value
            if not found:
                distance_val += 1
                
        return distance_val