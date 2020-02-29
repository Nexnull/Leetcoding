"""
Given an integer n, return the number of trailing(后面的，拖尾的) zeroes in n!.

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity时间复杂度为log(n)
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        25 20 15 10 5"""

        res = 0
        while n != 0:
            res += n // 5
            n //= 5
        return res

"""
time:O（log5n) space:O(1)
https://www.youtube.com/watch?v=88mG_huCxt0
这题让我们找一个数的阶乘的尾巴有多少个0
实际上就在问我们一个数的阶乘后面有多少个10
我们已知一个10 = 2 * 5, 因为1-9里面，2的倍数很多，2，4，6，8，他们乘5后面都有0
所以我们需要统计这个阶乘数，是由多少个5构成
例如5！，里面只有一个5，所以后面只有一个0
例如10！，里面有10，5，所以后面两个0
但是25，25=5*5，然后从25->0有5个5，所以后面有6个0（理解不了)
"""




