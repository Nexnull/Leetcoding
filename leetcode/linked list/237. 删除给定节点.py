# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

"""
脑经急转弯，因为我们没有head，所以不能用 pre.next = next这种做法来写
删除3
1>2>3>4>5
1>2>4>4>5(把3的值用4顶上，所以3消失了)
1>2>4>5（最后我们把多余的四去掉就好了）
"""