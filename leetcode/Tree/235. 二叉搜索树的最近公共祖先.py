"""
Given a binary search tree (BST), find the lowest common ancestor (LCA)最小公共祖先
 of two given nodes in the BST.
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        return root

"""
答案：
236的简化版，已知BST
1.假如说p,q的值小于root,说明这两个node在root的左子树，找
2.假如说p,q的值大于root,说明这两个node在root的右子树
3.假如终于发现分叉了，说明最小公共节点就是这个root
    或者是一个就是root,另一个小或大，那也不满足1，2的同小或同大
    
这种写法检查不了，p,q不在树上的情况，且能通过官方的所有测试条件
"""