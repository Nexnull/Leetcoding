

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        slow = pHead
        quick = pHead

        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
            if quick == slow:
                break

        if not quick or not quick.next:
            return None

        quick = pHead
        while quick != slow:
            quick = quick.next
            slow = slow.next


        return slow




"""
leetcode的142. Linked List Cycle II题目
这题其实在很多地方都做过，其实就是链表的快慢指针，一个指针一次走1，一个指针一次
走2，

问题，在这里我们并不知道怎么判断这个链表有没有环：
我觉得应该是起码得有三个node能形成一个环

答案：
数学太复杂，就直接记忆好了：

1。设置快慢指针遍历，当他们相遇了，则break循环
2。如果快慢指针有其一为none,则需要return None(判断有没有环)
3。使用快慢指针，如果相遇了，那么把一个指针调整到头部，两个指针每次都一步走，重新开始再相遇即可。
"""