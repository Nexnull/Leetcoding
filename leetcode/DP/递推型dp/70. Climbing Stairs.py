"""
给一个n阶的楼梯，一次你能下一层或两层
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x , y = 1, 1
        for _ in range(1,n):
            x , y = y, x+y
        return y