"""
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, head1, head2):
        if not head1 and not head2:
            return None
        if not head1:
            return head2
        if not head2:
            return head1

        new = head = ListNode(0)
        while head1 and head2:
            if head1.val <= head2.val:
                new.next = head1
                head1 = head1.next
            else:
                new.next = head2
                head2 = head2.next
            new = new.next

        if head1:
            new.next = head1
        if head2:
            new.next = head2

        return head.next





"""
感觉这题想要的做法应该是在原链表上操作
看了下自己的答案,发现跟自己的想法差不多，但是有些需要注意的地方

答案：
创建一个新node作为开头，然后同时遍历两个链表，那个链表的node
小就连在new的后面，直到有一个链表被遍历完。然后把剩下没遍历完的
给连上去

注意：
1.创建 new = head = ListNode(0),两个变量
new 是用来走遍历的，head是用来提交答案，head代表合并链表后的头节点

2.在while 循环里，注意每次循环结束以后都要把new = new.next一下

3.返回的时候返回的是head.next,因为第一个节点ListNode(0）是不算在
原来的链表里面的

"""