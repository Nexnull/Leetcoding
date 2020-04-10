# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        length = 0
        check = head
        while check:
            length += 1
            check = check.next

        pre = None
        cur = head
        for _ in range(length // 2):
            next = cur.next

            cur.next = pre
            pre = cur
            cur = next

        # 假如说链表长度为奇数， 那么我们的cur要往下走一步
        # 1 2 3(cur) 2 1
        if length % 2 == 1:
            cur = cur.next

        while cur != None and pre != None:
            if cur.val != pre.val:
                return False

            cur = cur.next
            pre = pre.next

        return True


"""
https://algocasts.io/episodes/VXGOqWQd
Time: O(n), Space: O(1)
这种方法是最优解，我们先用一个变量来记录链表的总长度
然后反转前半段链表， 然后pre,从中间向左走， cur从中间向右走
一次次来进行比

"""
