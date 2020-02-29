
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num != 0 and num &(num-1) == 0 and num & 1431655765== num


"""
答案
https://leetcode.com/problems/power-of-four/discuss/80461/Python-one-line-solution-with-explanations
这题同样可以用与power of 2 的两种方法来做
方法1，循环求解，不提
方法2，
1.与算power of two类似，一个power of 4的数在二进制中一定只有一个1
所以有了前两步：num != 0 and num &(num-1) == 0
2.但是4的倍数不同于2的倍数，4是(00100,0010000)它是只在偶数位上出现的，所以我们需要
num & 1431655765== num.来看看1是否在偶数位上
1010101010101010101010101010101 (1431655765)
"""

