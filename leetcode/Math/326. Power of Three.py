"""
问n是不是power of 3
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: return True
        if n < 3: return False

        while n % 3 == 0:
            n /= 3
        return True if n == 1 else False

"""
与power of 2原理一样
"""
