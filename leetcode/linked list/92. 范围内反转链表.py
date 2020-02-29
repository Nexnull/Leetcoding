"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head: return None

        pre = None
        nex = None
        cur = head

        while m > 1:
            pre = cur
            cur = cur.next
            m, n = m - 1, n - 1

        start = pre
        tail = cur
        # 这个反转链表，的开始反转点在一开始的cur,结束点在while后的pre

        while n:
            nex = cur.next


            cur.next = pre

            pre = cur
            cur = nex
            n -= 1

        # 此时，cur已经走到了第五位，但是pre还在第四位,我们需要把反转序列的尾node连到序列的头部
        # 把反转序列的头node,连到序列的尾部
        if start:
            start.next = pre
        else:
            head = pre

        tail.next = cur
        return head

"""
看答案：https://leetcode.com/problems/reverse-linked-list-ii/solution/
答案：
这题和反转链表挺不一样的，因为这题要求最后的指针都是正的，不像那题是反着的
于是我们有了最后处理这一步

1。重要的是
   开始时，pre在要反转序列以外，cur在反转序列的第一个node
   结束时，pre是在被反转链表里的最后一个node, 而cur不在反转的node里

2。本题关键在最后几步，我们要把 反转序列的最后一个node,练到头部，把反转序列的第一个node连到尾部
  这样才能形成一个正向的链表
"""
