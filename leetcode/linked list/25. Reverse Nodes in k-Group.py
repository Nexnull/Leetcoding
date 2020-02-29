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


"""
24是两个node两两交换，这个是多个node一起交换
于是我们可以看到用24的思维这题是比较难走的通的

"""