"""
就是一个最普通的二分查找。。
https://leetcode.com/problems/guess-number-higher-or-lower/description/
"""

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if guess(mid) == 0:
                return mid

            if guess(mid) == 1:
                left = mid + 1
            else:
                right = mid - 1
        return left
