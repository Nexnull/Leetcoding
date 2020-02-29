"""
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
"""
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num is None or num < 1:return False

        while num%2 == 0: num /= 2
        while num%3 == 0: num /= 3
        while num%5 == 0: num /= 5
        return num == 1

"""
https://algocasts.io/episodes/8eGx3mMO
Time: O(m+n+l), Space: O(1)
答案：
假如一个数是由2 3 5集合的乘积构成，那么它一定能满足上面的求解过程

注意：第一个丑数是1
"""