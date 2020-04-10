class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head

        while cur:

            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur

            cur = cur.next

        return dummy.next

"""
因为我们考虑到 1-1-1-1-2-3 然后要删除1的情况
所以我们要先准备一个DUMMY节点

其实这里有点小技巧，因为我们知道 我们要让 pre-> cur.next
我们不能先用while 遍历到 cur != val 的节点, cur本身就是不存在的, 所以cur 无法 = cur.next

我们能用一种更聪明的做法是， 不给cur = None的机会
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
"""