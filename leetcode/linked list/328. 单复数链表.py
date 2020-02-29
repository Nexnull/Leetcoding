"""
把一个链表，在index为单的，和index为双的，分别抽出来，然后拼在一起
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:return

        odd = head
        even = head.next
        evenHead = even

        while even != None and even.next != None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = evenHead

        return head

"""
https://leetcode.com/problems/odd-even-linked-list/discuss/78079/Simple-O(N)-time-O(1)-space-Java-solution.
其实只是设计到链表的操作
我们把单数链表连起来，再把双数链表连起来，最后把双数链表与单数链表连上，就好了
"""
