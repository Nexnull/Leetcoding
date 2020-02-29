"""
https://leetcode.com/problems/linked-list-cycle/
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast , slow = head , head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if fast is None or fast.next is None:
            return False

        return True

"""
141，只是判断有没有环。有返回true,无返回false
快慢指针来做吧，
假如说没环，那么fast就会遍历到None
假如说有环，快慢指针就会在环内相遇
出了循环判断一下是fast，fast.next遍历到尾部了还是真的两节点真相遇了

"""