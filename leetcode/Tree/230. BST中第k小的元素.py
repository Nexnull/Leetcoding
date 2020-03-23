# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def kthSmallestStack(self, root, k):
        res = 0
        stack = []

        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop(-1)
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right


class Solution1(object):
    def __init__(self):
        self.res = []

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.helper(root)
        return self.res[k - 1]

    def helper(self, root):
        if not root:
            return

        self.helper(root.left)
        self.res.append(root.val)
        self.helper(root.right)
"""
我们对这题考虑使用中序遍历法，因为是按顺序的
递归：
时间复杂度：O(N)，遍历了整个树。
空间复杂度：O(N)，用了一个数组存储中序序列。

非递归：
时间复杂度：O(N)，遍历了整个树。
空间复杂度：O(N)，用了一个数组存储中序序列。
"""


