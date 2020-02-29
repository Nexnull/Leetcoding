"""

Given a linked list, swap every two adjacent nodes
and return its head.

You may not modify the values in the list's nodes,
only nodes itself may be changed.

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        pre, pre.next = self , head

        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next , a.next , b.next = b, b.next, a


            pre = a
        return self.next

    def prt(self):
        print("hello")
        print(self)
        a = self
        a.next = 1
        print(self.next)




"""
这题其实非常简单暴力
其实就是每次选两个node交换好就好了

答案：
1.这题需要三个指针，pre代表两个交换元素前面的指针
pre.next , pre.next.next代表两个需要交换元素的指针

2。a = pre.next  b = pre.next.next

-1 -> 1-> 2-> 3

-1 -> 2-> 1-> 3

我们现在能看到为什么需要三个指针
补充知识：
1.python的连续运算
例如此题的： pre.next , b.next, a.next = b,a,b.next
其实等号的右边的变量是锁定好的，不会随着你左边的赋值而改变
直到这次运算的完成

所以这个行代码非常直观得帮我们解决了这道题

2.pre = self是什么意思？
这里的self，指的是Solution这个class,但是这里我们可以把它看作是一个Node，
因为我们并不需要去使用它，我们只需要使用self.next
self.next是可以自由设定的，存放什么值都无所谓，所以就等于用self.next来链接这个
class和第一个node

"""
if __name__ == "__main__":
    solution = Solution()
    # solution.swapPairs(3)
    solution.prt()
