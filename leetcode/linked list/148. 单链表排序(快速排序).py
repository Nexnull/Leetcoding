class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.quickSort(head, None)
        return head

    def swap(self, node1, node2):
        node1.val, node2.val = node2.val, node1.val

    def quickSort(self, head, end):
        if head == end or head.next == end: return
        pivot = head.val
        slow = head
        fast = head.next

        while fast != end:
            if fast.val <= pivot:
                # slow 向前走一步，指向一个大于pivot的值
                slow = slow.next
                self.swap(fast, slow)
            fast = fast.next

        # 遍历结束，把pivot换到中间，现在就是pivot左边都是小的，右边都是大的
        self.swap(head, slow)
        self.quickSort(head, slow)
        self.quickSort(slow.next, end)

"""
https://algocasts.io/episodes/eAGQ1lG4
答案：
1.这题的解法非常巧妙，在链表上运用了快速排序，其实想想也是没有问题的，因为我们
不需要去移动节点，我们只需要更换链表上node的值。其实原理跟快排还是一样的
"""