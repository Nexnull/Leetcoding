"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop(-1)
            res.append(node.val)

            for i in range(len(node.children)-1,-1,-1):
                stack.append(node.children[i])

        return res

"""
先序遍历 root, left , right
所以加进stack 的顺序是 right ,left

"""