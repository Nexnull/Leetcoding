"""
拍平二叉树
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:
"""
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return None
        self.prelist = []
        self.preOrder(root)

        cur = root
        for i in range(1,len(self.prelist)):
            cur.left = None
            cur.right = self.prelist[i]
            cur = cur.right

        return root



    def preOrder(self,root):
        if root is None: return None
        self.prelist.append(root)
        self.preOrder(root.left)
        self.preOrder(root.right)



"""
时间 O(n),遍历n个点，循环n个node , 空间  O(n)，建了一个长度为n的list
这题其实不难
1.就是先用前序遍历把所有的节点都加进一个list
2.然后遍历这个list,从root出发，因为这个list都是前序遍历来的
    所以我们把每个拿出来的node.right = 设为下一个点就好了
"""