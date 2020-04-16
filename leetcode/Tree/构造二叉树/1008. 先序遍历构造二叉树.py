# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        root,left,right
        """
        if not preorder:
            return None

        val = preorder.pop(0)
        root = TreeNode(val)

        split_index = 0
        for _ in range(len(preorder)):
            if preorder[split_index] < val:
                split_index += 1

        root.left = self.bstFromPreorder(preorder[:split_index])
        root.right = self.bstFromPreorder(preorder[split_index:])

        return root

"""
https://www.youtube.com/watch?v=Iup6Wl4bybY
其实这题的做法和别的构造二叉树差不多， 但是要注意的一点是，我们还是要去找出一个左右子树的分界来进行分割 
所以这就多了中间的那个for 循环，来进行查找

"""