"""
 Init a singly linked list [1,2,3].
 getRandom() should return either 1, 2, or 3 randomly.
Each element should have equal probability of returning. solution.getRandom();
以相同的概率返回回链表里的任意一个node
"""
from random import random


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        res = self.head.val
        cur = self.head.next
        count = 2

        while cur != None:
            if random() <= 1.0 / count:
                res = cur.val

            count += 1
            cur = cur.next
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

"""
答案：
1.这题的思想和398基本一样，注意count++的位置，因为cur = head的时候，count就已经=1了，
                                        所以当cur = head.next的时候，count就要是2了
                                         
"""