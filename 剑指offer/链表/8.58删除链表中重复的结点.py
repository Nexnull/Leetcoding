"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
**重复的结点不保留** .返回链表头指针。
 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        if pHead is None:
            return
        first = ListNode(-1)
        first.next = pHead
        cur = first
        nex = pHead

        while nex and nex.next:
            # 假如说没有重复，那么cur 和 next就正常的往下走
            if nex.val != nex.next.val:
                cur = cur.next
                nex = nex.next
            # 假如说有多个重复，那么 nex就一直往后找，知道找到第一个不重复的，然后cur.next = nex
            else:
                same = nex.val
                while nex and same == nex.val:
                    nex = nex.next
                cur.next = nex

        return first.next



"""
这题我有印象，用常规的两个快指针去查重复，一个留在没重复的
node是没用的。不对，这个方法是对的，但我这样写不对
在nex.val == nex.next.val时
对nex的处理不对
不能写：nex = nex.next.next, 因为假如说三个数连在一起时
则会出bug

1->2->3->3->3->4->4->5
               n
               c
答案：
1.为什么cur赋值成链表外的元素呢？
因为cur是用来定下已经确定的值，我们还没有判断链表的第一个元素是不是重复，所以不能把cur赋值

2.while里的第一个循环，是最后的检查机制
因为我们在下面写了 cur.next = nex，只是确认了nex已经跨越了前面的重复
但我们并不知道nex后面有没有重复
例如3,3,4,4，现在nex已经到了4
所以我们要在if nex.val != nex.next.val做个最终判断，判断后面已经没有重复了
才把cur = cur.next给定下来

注意：!!
这里cur 一定要比 nex 慢一步。因为 cur一定是要停留在完全没有重复的节点上，
但是nex是要探查有重复的节点，所以必须要等nex先到一个没有重复的节点以后，我们才能 cur.next = nex

1 3 3 5
假如说cur和nex一样的话，那么这个3也会被记录进去
但nex比cur快一步的话，nex就会发现 3 3是重复的，nex到了5以后，cur.next 才等于nex
"""