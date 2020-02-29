class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head: return head

        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:

            if cur.next.val == cur.next.next.val:
                val = cur.next.val
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

"""
https://www.youtube.com/watch?v=w16pq8_DVno
0-1-2-3-3-4-4-5
我们先创建dummy节点0，cur从dummy开始（因为我们不确定第一个和第二个node有没有重复）
这题的去重办法是，cur所在的位置是绝对没有重复的，我们要用cur.next,和cur.next.next去探测重复
最终目的是要达到，cur.next所在的位置是没重复的（cur.next.val != cur.next.next.val),才能让cur移过去
0-1-2-3-3-4-4-5
    c         c.next


在cur.next.val == cur.next.next.val的情况下：
val来记录当前cur.next的值
从而来移动cur.next的指针指向一个不等于val的值
例如 0-1-2-3- 3- 4- 4-5
          val   c.n
cur.next得移动到4我们才停止移动cur.next
然后再进入新一轮的cur.next.val == cur.next.next.val判断
"""