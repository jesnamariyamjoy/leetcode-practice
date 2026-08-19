class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10
            rev = rev * 10 + digit

            # check overflow before it actually happens
            if rev > INT_MAX:
                return 0

        rev *= sign
        return rev if INT_MIN <= rev <= INT_MAX else 0