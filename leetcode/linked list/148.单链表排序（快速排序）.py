class Solution:
    def sortList(self, head: ListNode):
        if not head or not head.next:
            return head

        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        mid, slow.next = slow.next, None # save and cut.

        # 分而治之
        left, right = self.sortList(head), self.sortList(mid)

        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next

        h.next = left if left else right
        return res.next

"""
就是一般归并排序的做法
首先通过快慢指针找到链表的中间节点
然后分出两段链表，分别来进行递归
最后拿到left,right两段排序好的链表，来进行融合
"""
