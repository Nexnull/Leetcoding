"""
判断从最上面的根节点到最下面的叶节点，是否存在一条路，使得他们的和等于sum

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        return self.helper(root, sum)

    def helper(self, root, sum):
        if not root:
            return False

        if root.val == sum and not root.left and not root.right:
            return True

        return self.hasPathSum(root.left, sum - root.val) or \
               self.hasPathSum(root.right, sum - root.val)

"""
答案：
还是切树三件套，helper, if not root, 以及终止条件
"""