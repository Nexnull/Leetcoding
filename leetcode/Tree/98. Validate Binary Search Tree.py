"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
判断这棵树是不是二叉搜索树
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#1
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return
        return self.helper(root, -float('inf'), float('inf'))

    def helper(self, root, min, max):
        if not root:
            return True

        if min != None and root.val <= min: return False
        if max != None and root.val >= max: return False
        return self.helper(root.left,min,root.val) and self.helper(root.right,root.val,max)

#2
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.prevalue = None
        return self.helper(root)

    def helper(self, root):
        if not root:
            return True

        if not self.helper(root.left):
            return False

        if self.prevalue and root.val <= self.prevalue.val:
            return False
        self.prevalue = root

        return self.helper(root.right)

#3
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = list()
        self.validation(root)
        # and 一个len(set())是防止出现【1，1】这种情况
        return self.res == sorted(self.res) and len(set(self.res)) == len(self.res)

    def validation(self, root):

        if not root:
            return
        else:
            self.validation(root.left)
            self.res.append(root.val)
            self.validation(root.right)
"""
答案：
有三种解法：
1。给个把root,他所应当的最大值，和最小值给放进去。假如在左子树，那么左子树的每个点都不可以大于root.val
假如在右子树，那么每个node。都不能小于root.val 。 遍历到node == None 就返回True
2.BST我们就要想到中序遍历法，这个中序遍历法在于，跑一个中序遍历，且记录每上一次循环的node,当前的root.val > pre.val，假如说不符合则返回false.然后其中有很多奇奇怪怪的限制条件，水平不够，最好别写这个，怕错了
3。我们可以直接跑一个中序遍历，然后记录下每一个值，直接对比一下它是不是递增的，利用sort(res) == res来比 

"""