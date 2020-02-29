"""
从尾到头打印链表
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if ListNode == None:
            return None

        container = []
        while listNode:
            container.insert(0,listNode.val)
            listNode = listNode.next
        return container





"""
答案：
可以手动写一个list来实现一个列表,每次insert都插入在0的位置，使得先进去的元素反而在后面

"""