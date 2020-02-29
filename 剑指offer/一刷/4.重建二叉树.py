"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树
。假设输入的前序遍历和中序遍历的结果中都不含重复的数字
。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}
则重建二叉树并返回。

"""

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

        root.left = self.reConstructBinaryTree(pre ,tin[:index])
        root.right = self.reConstructBinaryTree(pre, tin[index+1:])
        return root


"""
这题的关键是：
1。我们要搞清楚为什么他们要给我们一个中序遍历，和一个前序遍历的的点
    因为中序遍历给你的作用就是让你找到整棵树的第一个node（定位）
    前序遍历是给你用来做递归的，来重建二叉树的（排序）
2。为什么每次我们递归都是pre放进去，而不用更改？
    重建时先建立左子树时，会将pre中的内容一个个pop掉，
    这样到建立右子树时，pre中已经不包含左子树中的内容了。

答案：
先续遍历，root left right , 所以整个列表是[root,left,right]
中续遍历，left root right, 所以tin列表是[left,root,right]


1。我们先找出，整个树最中心的root,然后用它来做第一个点，
2。然后把这个root的定位找出来，index的左边就是左子树，右边是右子树，
3。我们让root.left,root.right递归
我们把左子树的node切好片，把右子树的node也切好片，把他们放进递归
4。return node

"""