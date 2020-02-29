"""
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, root):

        if root == None:
            return False

        return self.helper(root.left, root.right)

    def helper(self,left,right):
        if not left and not right:
            return True
        if left and not right:
            return False
        if not left and right:
            return False
        if left.val != right.val:
            return False

        return self.helper(left.left, right.right) and \
               self.helper(left.right , right.left)



"""
回忆起二叉树的镜像那道题，那题要做的很简单，遍历的每一个点都 left,right = right,left
这题要做的是看似简单，其实不简单
没什么想法

答案：
1.注意这个helper是要放两个node作为参数的

一刷借鉴的那个答案比较简洁，二刷自己写的比较乱

"""