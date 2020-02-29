class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, head):
        if not head:
            return None

        pre, next = None, None
        while head:
            next = head.next
            head.next = pre

            pre = head
            head = next

        return pre





"""
怎么反

答案：
    1->2->3

设计变量 pre = None , next = None ,head = 1
pre是用来让head通过.next来反转的变量
next是用来记录head下一个位置的变量
head就是我们当前操作的那个节点


1. next = 1.next = 2

           next
               \
            1->2->3

在这里把链表进行反转，且记录好head.next，因为后面要把它赋值给head
2. 1.next = pre

            next
               \
       pre<-1  2->3
       

下一步等于把这三个指针都往后移了一个单位
3.pre = head
  head = next
  以及每次循环开始是的next = head.next
  
为什么最后返回的是pre呢。因为当head == None时终止循环，而我们设定的顺序是 pre->head->next
所以pre是链表的最后一个元素了
"""