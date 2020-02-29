class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        fast = head
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow


"""
https://algocasts.io/episodes/4rpa6aWZ
Time: O(n), Space: O(1)
这题使用一个快慢指针，就能完成一次遍历就能找出所有结果

"""