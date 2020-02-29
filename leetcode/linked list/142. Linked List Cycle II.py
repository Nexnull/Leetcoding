"""
https://leetcode.com/problems/linked-list-cycle-ii/
Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        quick = head
        slow = head
        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
            if quick == slow:
                break

        if quick is None or quick.next is None:
            return -1

        fast = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return fast






"""

查看环状链表的入口节点
还是使用快慢指针：
1。若快慢指针能走完全程，则说明没有环，返回-1
2。若没走完，且在环内相遇，则把快慢指针的其中一个设为头节点，然后两个指针一步一步走
走到相遇的地方就是环的入口

remark:
1.尚且搞不清楚leetcode的运行机制，反正没有头两行就是一定过不了，但是我不是已经写了
检测机制了吗？？？

"""