# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return

        return self.helper(0, len(nums) - 1, nums)

    def helper(self, start, end, nums):
        if start > end:
            return

        mid = (start + end) // 2
        root = TreeNode(nums[mid])

        root.left = self.helper(start, mid - 1, nums)
        root.right = self.helper(mid + 1, end, nums)

        return root


"""
时间复杂度：每个元素只访问一次。o(N)
空间复杂度：二叉搜索树空间 O(N)，递归栈深度 O(logN)。

https://algocasts.io/episodes/rLmP98Go
我们似乎不用太过例会这个mid 到底是在正中间，还是在正中间偏左， 正中间偏右
因为是二叉搜索树，偏左还是偏右体现的差别应该是左子树多一个节点 还是右子树多一个节点

"""