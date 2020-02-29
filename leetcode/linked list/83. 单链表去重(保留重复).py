# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head: return
        cur = head

        while cur:

            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next

            cur = cur.next

        return head

"""
这题我们用不断更新head.next, 知道head.next到达一个不等于先前数的位置
然后才把head指针移向head.next
"""