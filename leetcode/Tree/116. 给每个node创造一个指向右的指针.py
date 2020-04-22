"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        level_start = root

        while level_start != None:
            cur = level_start
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next != None:
                    cur.right.next = cur.next.left

                cur = cur.next
            level_start = level_start.left

        return root

"""
https://www.youtube.com/watch?v=_RMIQ3hDTQs
答案：

"""