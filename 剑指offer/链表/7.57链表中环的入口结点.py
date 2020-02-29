"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        slow = pHead
        quick = pHead

        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                break


        if quick == None or quick.next == None:
            return None

        quick = pHead
        while quick != slow:
            quick = quick.next
            slow = slow.next
        return quick

"""
答案：
1.设置快慢指针，如果顺利走出循环，且quick ,quick.next == None,说明
这是不包含环的

2.如果顺利走出循环，也有可能是quick == slow
那么我们需要把这两个指针的任意一个设为头指针 quick = head
然后两个指针一步一步走，相交的那个点为环的入口节点

注意：
    1。这里的判断语句一定要写在两次赋值后面，因为一开始slow,quick
    都是相等的，会导致后面出错
    while quick and quick.next:
        if slow == quick:
            break
        slow = slow.next
        quick = quick.next.next
        
    
        

"""