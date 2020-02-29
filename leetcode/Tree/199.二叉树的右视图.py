# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        self.res = []
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, level):
        if not root:
            return

        if level == len(self.res):
            self.res.append(root.val)

        self.dfs(root.right, level + 1)
        self.dfs(root.left, level + 1)

"""
https://www.youtube.com/watch?v=_iKUgRiUYKA
On On
原理很简单：
因为我们只要同一层的最右边节点，所以我们就把len(res) 和 level
对应起来，保证每一层我们只记录最右边的节点

然后因为我们要最右边的节点，所以递归的时候优先递归右边，右边没有，再递归左边
"""