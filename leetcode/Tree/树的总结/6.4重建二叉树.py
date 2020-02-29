class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None

        root = TreeNode(pre.pop(0))
        index = tin.index(root.val)

        root.left = self.reConstructBinaryTree(pre,tin[:index])
        root.right = self.reConstructBinaryTree(pre,tin[index+1:])

        return root


"""
这题有点印象
已知先序遍历： root , left ,right
    中序遍历: left , root ,right
于是我们就可以先先找到root，就是先序的第一个元素



"""
