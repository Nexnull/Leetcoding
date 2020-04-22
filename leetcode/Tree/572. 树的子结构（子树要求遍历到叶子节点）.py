# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isSubtree(self, s, t):
        if not s:
            return False
        if self.helper(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def helper(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False

        return s.val == t.val and self.helper(s.left, t.left) and self.helper(s.right, t.right)

"""
这题与剑指offer的解法不太一样

"""