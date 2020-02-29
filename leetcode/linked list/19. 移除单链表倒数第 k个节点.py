class Solution(object):
    def removeNthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        front = head
        last = head

        while front.next != None and k:
            front = front.next
            k -= 1

        if k != 0: return head

        while front.next != None:
            front = front.next
            last = last.next

        last.next = last.next.next
        return head

"""
https://algocasts.io/episodes/eAGQQlG4
这题和寻找 链表的中间节点是同一道题
注意：
1. 我们进行while 循环的时候，要while front.next: 这样front才不会 = None
2. 假如说k 超过链表长度的话，那我们直接返回整个链表就好了


"""