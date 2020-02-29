"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k <= 0:return head

        length = 1
        count = head
        while count.next != None:
            length += 1
            count = count.next
        count.next = head

        k = k % length
        newend = head
        for i in range(length - k - 1):
            newend = newend.next

        newhead = newend.next
        newend.next = None
        return newhead
"""
// Time: O(n), Space: O(1)
我感觉这题和双指针的关系并不大把
1.一开始我们先要计算出链表的长度，利用count指针。数到最后记得要把末节点的和头节点连起来
2.我们要对k 取膜，是用来应对 k > length的情况，避免过度循环
3.定的新链表指针，newend,把它遍历到 n - k的位置
（注意，因为newend一开始就等于在0的位置，所以我们遍历到n-k-1就好了）
4.找到new end,把newend.next 设成新的头
5.然后newend指向空，完成新链表
"""