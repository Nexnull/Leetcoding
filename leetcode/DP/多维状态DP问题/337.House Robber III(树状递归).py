# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.helper(root)
        return max(res[0], res[1])

    def helper(self, root):
        # 0 is not rob current
        # 1 rob current
        if root == None:
            return [0, 0]

        temp = [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        temp[0] = max(left[0], left[1]) + max(right[0], right[1])
        temp[1] = left[0] + right[0] + root.val

        return temp

"""
https://www.youtube.com/watch?v=-i2BFAU25Zk
这题是树状递归
每个节点我们都创造一个数组，temp,
temp[0]代表不抢劫当前node的最大值
temp[1]代表，抢劫当前node的最大值
我们通过left,right递归完后面的所有节点，来往上推，就能得到temp两种选择的最值
最后我们返回两种选择中的较大值即可
"""

