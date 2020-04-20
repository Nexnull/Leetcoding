class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0

        #剪枝
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)

        #剪枝
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)

        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

"""
https://algocasts.io/episodes/BPp6aZGr
Time: O(n), Space: O(n)
面对这种题，我们可以想象一下一种做法就是 用前中后序遍历去走每一个节点，然后把在范围内的节点都加在一起

但是这样时间复杂度就高了，所以更好的办法就是，我们利用一种剪枝的手法，去把不可能符合结果的节点排除掉
这样就能解决问题了
"""