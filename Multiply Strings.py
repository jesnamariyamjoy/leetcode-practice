class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
            
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                
                # Current product plus existing value at position p2
                total = mul + pos[p2]
                
                # Carry goes to p1, remainder stays at p2
                pos[p2] = total % 10
                pos[p1] += total // 10
                
        # Convert result array to string, skipping leading zeros
        result = "".join(map(str, pos))
        return result.lstrip("0")