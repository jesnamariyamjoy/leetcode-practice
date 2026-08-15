class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        bed = flowerbed
        length = len(bed)
        
        for i in range(length):
            if bed[i] == 0:
                left_empty = (i == 0) or (bed[i - 1] == 0)
                right_empty = (i == length - 1) or (bed[i + 1] == 0)
                
                if left_empty and right_empty:
                    bed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        
        return count >= n