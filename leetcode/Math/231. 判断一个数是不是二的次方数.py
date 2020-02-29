"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n != 0 and n&(n-1) == 0


def isPowerOfTwo(self, n):
    """
    :type n: int
    :rtype: bool
    """
    if  n < 1:
        return False
    while n % 2 == 0:
        n /= 2
    return True if n == 1 else False

"""
三个方法：
1.%2,不断%,判断余数
2。log2 是否为整数,pytho的方法似乎只能返回浮点数 time:O(logn)

重要！
3。利用 x&(x-1) time:O1
因为凡是2的次方数，一定都只有一个1，例如2，4，8，16。。 
而x-1 是除当前位置为1以外，别的位置全是1的数，例如
x =   1000
x-1 = 0111
x&(x-1) = 0000
"""