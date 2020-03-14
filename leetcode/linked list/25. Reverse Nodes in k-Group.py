"""
https://leetcode.com/problems/reverse-nodes-in-k-group/
Given a linked list, reverse the nodes of a linked list k at a time and
return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
 If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        pre = None
        cur = head
        next = None
        check = head

        can_process = 0
        count = 0

        while can_process < k and check != None:
            check = check.next
            can_process += 1

        # 剩余节点大于等于k，进行反转
        if can_process == k:
            # 反转链表模版
            while count < k and cur != None:
                next = cur.next

                cur.next = pre

                pre = cur
                cur = next
                count += 1

            # 说明还没遍历到原链表的最尾节点，cur和next现在指向的是已反转部分的后一个节点
            # pre指向反转部分的最后一个节点
            # 1>2>3>4>5>6  =>  1(head)<2<3(pre)  4<5<6(pre,head.next)
            if next != None:
                head.next = self.reverseKGroup(next, k)

            # pre永远是反转链表的最后一个部分
            return pre


        # 剩余节点小于k，不能进行反转
        # 1(head)<2<3 4(head.next)>5, 我们让1.next = 4
        else:
            return head

"""
24是两个node两两交换，这个是多个node一起交换
于是我们可以看到用24的思维这题是比较难走的通的

"""