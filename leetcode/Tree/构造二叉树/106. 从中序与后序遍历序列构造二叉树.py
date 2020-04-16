# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        # left root right      left right root
        if not inorder or not postorder:
            return None

        val = postorder.pop(-1)
        root = TreeNode(val)
        i = inorder.index(val)

        root.right = self.buildTree(inorder[i + 1:], postorder)
        root.left = self.buildTree(inorder[:i], postorder)

        return root

"""
对于这种题， 我们首先先要把root节点找出来， 然后进行左右分堆递归
因为 postorder是 left, right, root, 所以把root抽出来后， 下一个节点是right的
所以我们要把先遍历右子树
然后才遍历左子树
"""