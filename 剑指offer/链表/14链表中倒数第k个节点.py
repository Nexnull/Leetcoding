"""
输入一个链表，输出该链表中倒数第k个结点。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head:
            return None

        fast = head
        slow = head

        for i in range(k):
            if fast != None:
                fast = fast.next
            else:
                return

        while fast:
            slow = slow.next
            fast = fast.next
        return slow




"""
记住这个答案把，没什么好说的
代码思路如下：
两个指针，先让第一个指针和第二个指针都指向头结点，
然后再让第一个指正走(k-1)步，到达第k个节点。然后两个指针同时往后移动，
当第一个结点到达末尾的时候，第二个结点所在位置就是倒数第k个节点了。。
0    k    len-k  len
   len-k    k     len

"""