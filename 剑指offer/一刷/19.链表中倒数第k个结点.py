class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        front = head
        last = head
        print(head.val)
        # while front != None and count < (k-1):
        for i in range(k):
            if front == None:
                return
            elif front == None and i == k:
                return head
            front = front.next


        while front.next != None:
            front = front.next
            last = last.next

        print(last.val)
        return last.next



if __name__ == "__main__":
    solution = Solution()

    node3 = Node(3, None)
    node2 = Node(2,node3)
    node1 = Node(1, node2)
    solution.FindKthToTail(node1,1)




"""
说实话没什么想法
但是感觉应该不难

我的思路：
其实硬是要做也可以，先统计一边这个链表有多少个node,最后len - k ,就是要找的那个node了。
事实上确实有类似的做法，而且效率很高，他们是把每个node都存在一个list里，返回list[-k]

网上思路：
代码思路如下：两个指针，先让第一个指针和第二个指针都指向头结点，
然后再让第一个指正走(k-1)步，到达第k个节点。然后两个指针同时往后移动，
当第一个结点到达末尾的时候，第二个结点所在位置就是倒数第k个节点了。。
0    k    len-k  len
   len-k    k     len
"""