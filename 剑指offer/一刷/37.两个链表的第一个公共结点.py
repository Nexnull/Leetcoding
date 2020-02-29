# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        cur1 , cur2 = pHead1 , pHead2

        while cur1 != cur2:
            cur1 = cur1.next if cur1 != None else  pHead2
            cur2 = cur2.next if cur2 != None else  pHead1
        return cur1





if __name__ == "__main__":
    solution = Solution()
    solution.FindFirstCommonNode()



"""
记得做过，但是不记得怎么做了

做法：
这道题和160.Intersection of Two Linked Lists是一样的。都是求两个链表的第一个公共结点。
方法一：

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

时间复杂度O(m+n)，空间复杂度O(m+n)。
"""