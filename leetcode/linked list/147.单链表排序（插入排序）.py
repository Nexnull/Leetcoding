# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = head

        while cur != None:
            p = dummy
            cur_next = cur.next

            while p.next != None and p.next.val <= cur.val:
                p = p.next

            cur.next = p.next
            p.next = cur
            cur = cur_next

"""
Time: O(n^2), Space: O(1)
https://algocasts.io/episodes/XZWvVNW7
答案：
1.这题使用了插入排序，于此同时我们要新建一个链表来存放排序好的node
2. 插入排序的做法就是，把无序区的元素一个个拿出来，放到有序区一个个位置来对比，最后插入到合适的位置

  本题插入做法  p -> p.next ,  p -> cur -> p.next
3.我们用cur_next 来储存原链表的进度,用于找到无序区的下一个元素
4.注意 while 那里，要先把p.next != None 先进行判断，因为and 是从左执行到右边的

"""