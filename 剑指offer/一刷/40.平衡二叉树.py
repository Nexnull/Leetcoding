


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        self.flag = True
        self.helper(pRoot)
        return self.flag



    def helper(self,node,):
        if node == None or self.flag == False:
            return 0

        left = self.helper(node.left)
        right = self.helper(node.right)

        if abs(left - right) > 1:
            self.flag = False
        return left + 1 if left > right else right + 1


"""
平衡二叉树（Balanced Binary Tree）它是一棵空树或它的左右两个子树的高度差的绝对值不超过1,意味着其中一边可以是缺一个node的。
这题的做法是要计算每个node的高度差

我的想法：怎么计算高度差。没想法

答案：从上往下，看每个顶点的左右高度差，用二叉树的深度的答案来求
https://blog.csdn.net/u010005281/article/details/79718391
"""