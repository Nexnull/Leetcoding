# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root: return

        if root.left and not root.left.left and not root.left.right:
            self.res += root.left.val

        self.helper(root.left)
        self.helper(root.right)

"""
答案：
本题关键，我们如何找到每一个左叶子：
if root.left and not root.left.left and not root.left.right
这个判断语句非常重要，自己领悟一下
"""