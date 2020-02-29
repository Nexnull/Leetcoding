"""
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0); p = res
        p1, p2, carry = l1, l2, 0
        while p1 != None or p2 != None or carry != 0:
            sum = carry
            carry = 0
            if p1 != None:
                sum += p1.val
                p1 = p1.next
            if p2 != None:
                sum += p2.val
                p2 = p2.next

            if sum >= 10:
                sum %= 10
                carry = 1

            p.next = ListNode(sum)
            p = p.next
        return res.next

"""
https://algocasts.io/episodes/JNmDRpOZ
Time: O(max(m, n)), Space: O(max(m, n))
答案:
1.主要要知道怎么操作carry（进位）,当sum>=10时我们有进位
于此同时把carry = 1,然后在下一次循环开始再sum = carry,carry = 0
2.一些链表的操作，p.next = ListNode(sum)
"""


