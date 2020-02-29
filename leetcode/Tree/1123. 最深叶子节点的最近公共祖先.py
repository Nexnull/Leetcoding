# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.helper(root)[1]

    def helper(self, root):
        if not root:
            return 0, None

        dl, left = self.helper(root.left)
        dr, right = self.helper(root.right)

        # 发现左边比右边深，那我们就不用看右边了
        if dl > dr:
            return dl + 1, left
        # 发现右边比左边深，我们就不用看左边了
        elif dl < dr:
            return dr + 1, right
        # 发现左右一样深，就返回当前节点
        else:
            return dl + 1, root


"""
https://www.youtube.com/watch?v=Up8iyOrq-5Y
答案：
主要这题你得了解它的判定规则
假如说 1
     2  3 那么他们的最深叶子节点的公共祖先就是1
     
       1
     2   3
    4
    最深叶子节点是4，所以它要返回自己，它自己就是最深叶子节点的最近公共祖先
    
       1
     2   3
    4  5
    对于这个节点的话，它的最深叶子节点的公共祖先就是2
    
这题怎么看是不是最深叶子节点，就要从depth这个变量来说起
三个判断语句
    


"""