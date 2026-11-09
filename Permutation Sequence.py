import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = list(range(1, n + 1))
        factorial = math.factorial(n - 1)
        k -= 1  # Convert to 0-indexed
        
        result = []
        for i in range(n, 0, -1):
            index = k // factorial
            result.append(str(numbers[index]))
            numbers.pop(index)
            
            if i > 1:
                k %= factorial
                factorial //= (i - 1)
                
        return "".join(result)