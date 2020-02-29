"""
操作给定的二叉树，将其变换为源二叉树的镜像。
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11

    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5

"""

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        self.Swaphelper(root)

        return root

    def Swaphelper(self,root):
        if root != None:

            root.left , root.right = root.right , root.left
            self.Swaphelper(root.left)
            self.Swaphelper(root.right)












"""
这似乎是，在同一棵树上进行的操作，那么要怎么操作呢？
看节点的变化，左树的最左节点，要挪到右树的最右节点，感觉不是光操作node就可以了
应该需要用到一些数据结构来储存node
然后再反向赋值呢？
但是用递归的话，要怎么来

答案：
是我傻逼了，例如6 10 换了以后，下面子树不也跟着换了吗？
不需要用到任何数据结构
真的巨简单
"""