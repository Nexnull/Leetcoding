"""
输入两个链表，找出它们的第一个公共结点。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return

        new1 = pHead1
        new2 = pHead2

        while new1 != new2:
            if new1 == None:
                new1 = pHead2
            else:
                new1 = new1.next

            if new2 == None:
                new2 = pHead1
            else:
                new2 = new2.next
        return new1

"""
怎么查啊

答案：
1.new1,new2分别赋值为head1 head2
2.当new1 != new2的时候，不停止循环，这里跟树不一样，因为是公共节点所以那个节点的地址是固定的，所以可以直接 ==
3.当new为none时，让它与另一个head连上


我们可以把两个链表拼接起来，一个pHead1在前pHead2在后，一个pHead2在前pHead1在后。
这样，生成了两个相同长度的链表，那么我们只要同时遍历这两个表，就一定能找到公共结点。
有点像快慢指针

            a
              \ 
                c
              /   
     b1 -b2

a - c - b1 - b2 - c - b1 - b2 - c - b1 - b2- c
b1- b2- c  - a  - c -  a - c  - a - c  - a - c

我们可以发现，运用这种方法能使的c出现多次重叠，因为两个链表是非相等且循环，所以总有概率是能遍历
到相同点

时间复杂度O(m+n)，空间复杂度O(1)。

"""