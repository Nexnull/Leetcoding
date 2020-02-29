"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root: return res

        stack = [root]

        while stack:
            node = stack.pop(-1)
            res.append(node.val)

            for node in node.children:
                stack.append(node)

        return res[::-1]

"""
答案：
与145题一样，只要我们加进res的顺序是 root,right,left
那么最后我们把结果列表一反转，就变成了left,rigth,root

至于stack的处理，我们需要先加left,再加right,这样pop出来的顺序才是right,left

"""
