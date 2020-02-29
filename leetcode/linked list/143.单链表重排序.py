"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

Given 1->2->3->4, reorder it to 1->4->2->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        mid = self.findMid(head)
        l2 = mid.next
        # mid.next = None是因为mid是属于l1的，我们要让l1,l2的结尾都指向空
        mid.next = None

        l2 = self.reverseLinkedlist(l2)
        l1 = head

        while l1 and l2:
            next = l1.next

            # 把l1连到l2
            l1.next = l2

            # 移动l2指针
            l2 = l2.next
            # 把l2上的节点连到l1
            l1.next.next = next
            # 移动l1指针
            l1 = next

    def findMid(self, head):
        quick = head
        slow = head

        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next

        return slow

    def reverseLinkedlist(self, head):
        pre = None
        while head:
            next = head.next

            head.next = pre

            pre = head
            head = next
        return pre

"""
https://www.youtube.com/watch?v=3wa9fa4IhOU
1.先找到链表的中点，用快慢指针
2.然后从中点到最后，翻转后半段链表
    1->2->3->  <-4<-5
3.然后两个链表都从头开始，一个个next过去，形成1->5->2->4->3
"""