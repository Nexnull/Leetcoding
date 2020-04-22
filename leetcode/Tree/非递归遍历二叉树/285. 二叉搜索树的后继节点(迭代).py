# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # 情况1，p有右子树，我们要找到右子树的最左节点
        if p.right:
            p = p.right
            # 当p.left == None时，说明已经遍历到最后了
            while p.left:
                p = p.left
            return p

        stack = []
        pre = -sys.maxsize

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            # root 代表着pre节点的下一个节点
            root = stack.pop()

            # 假如说pre 节点 == p.val, 那么我们就把pre节点的下一个节点root给返回
            if p.val == pre:
                return root

            # 发现上面判断没查到的话，那么我们把当前节点的值放在pre里面
            # 继续遍历下去
            pre = root.val

            #继续遍历
            root = root.right

        return

"""
时间复杂度为 O(H_p)，其中 H_p 是节点 p 的高度。如果没有右孩子，时间复杂度为O(H)，其中H为树的高度。
空间复杂度：如果节点 p 有右孩子，空间复杂度为O(1)。如果没有右孩子，空间复杂度度为 O(H)。

https://leetcode-cn.com/problems/inorder-successor-in-bst/solution/er-cha-sou-suo-shu-zhong-de-shun-xu-hou-ji-by-leet/
因为是bst，所以它的后续节点肯定和中序遍历有关
两种情况：
1。p节点有右节点，那么p下一个节点一定是右节点的最左节点
2。p节点没有右节点，那么碰上这种情况就要用到常规的中序遍历的做法来处理
"""