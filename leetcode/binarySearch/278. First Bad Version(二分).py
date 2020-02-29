"""
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
 which causes all the following ones to be bad.

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
给你一串版本数，然后从某个数开始后面的版本都是坏版本，而前面的都是好版本，让你找出第一个坏版本
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:return 1

        left , right = 1, n

        while left <= right:

            mid = (left + right) //2
            if isBadVersion(mid) is False:
                left = mid + 1
            else:
                right = mid - 1

        if isBadVersion(left) == True: return left
        return right

"""
https://www.youtube.com/watch?v=8_2YbUniCMo
time O(logn) space O(1)
就是用二分查找来做的，根据题意很容易理解为什么要用二分查找
1.
"""