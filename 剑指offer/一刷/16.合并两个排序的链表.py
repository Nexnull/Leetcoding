class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1

        new = head = ListNode(0)
        while pHead1 != None and pHead2 != None:
            if pHead2.val > pHead1.val:
                new.next = pHead1
                pHead1 = pHead1.next
            else:
                new.next = pHead2
                pHead2 = pHead2.next

            new = new.next

        new.next = pHead1 or pHead2
        #当时漏了这一条，因为上面两个指针只要有一个到了none,就会终止，所有就肯定还剩一个
        #没有放进linklist

        return head.next






if __name__ == "__main__":
    solution = Solution()

"""
其实这题并不怎么难，主要就是语法不够熟悉，算法是极其简单的
答案：
1.我们需要创建一个新的节点，用来串联这两个链表
2.每连接一次，new,phead(1or2)都要同时next,来进行下一步的比较
3.当其中一个节点走完了，退出了循环，我们要记得把new.next = 另一个还没走完的节点
"""