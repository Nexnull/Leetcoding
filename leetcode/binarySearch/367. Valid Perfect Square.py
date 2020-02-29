"""
看leetcode69
"""

class Solution(object):
    def isPerfectSquare(self, x):
        """
        :type num: int
        :rtype: bool
        """
        if x == 0 or x == 1:
            return x

        left = 0 ; right = x ; res = 0
        while left <= right:
            mid = (left+ right)//2
            if mid*mid ==  x:
                return True
            elif mid > x // mid:
                right = mid - 1
            else:
                left = mid + 1
                res = mid

        return res*res == x

"""
改了return True的条件，因为当x//mid时有向下取整的可能
会导致类似 x = 5,但是返回True的情况

"""