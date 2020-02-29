"""
两个二进制数，每个位置上不同数 的数量的和
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        new = x ^ y
        count = 0
        while new != 0:
            count += 1
            new &= (new - 1)
        return count

"""
time:O(n) space:O(1)
答案：
1.首先先通过异或^ 找出x,y中不一样的数的位置（不一样的数那一位为1）
2.然后利用 new &= (new - 1) 能消除二进制位上最后面的一个1，重复操作以及计数，就能得到最后的答案
"""