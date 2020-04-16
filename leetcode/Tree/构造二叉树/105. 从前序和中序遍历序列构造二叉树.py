"""
前序遍历 preorder = [3,9,20,15,7]  root left right
中序遍历 inorder = [9,3,15,20,7]   left root right
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        # 因为前序遍历，第一个节点总是root， 找到root以后就要对他进行一个分界了
        root = TreeNode(preorder.pop(0))
        # 中序遍历中， 在root左边的就是左子树， 在root右边的就是右子树
        index = inorder.index(root.val)

        # 因为对于preorder来说， root left, 所以下一个节点是左子树的，所以就先递归左子树
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])
        return root
