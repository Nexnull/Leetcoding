class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        first = ListNode(-1)
        first.next = pHead
        cur = first
        nex = pHead


        while nex and nex.next:
            print(cur.val ,  nex.val,nex.next.val,"up")
            if nex.val != nex.next.val:
                cur = cur.next
                nex = nex.next
            else:
                val = nex.val
                """
                一个细节：
                我的写法：
                while val == nex.next.val:
                    nex = nex.next
                cur.next = nex.next
                
                正确写法：
                while nex and val == nex.val:
                    nex = nex.next
                cur.next = nex
                
                while nex and 可以帮助通过{1,1,1,1}这种情况，因为不加的话
                val != None 导致退出循环，然后cur.next = None导致报错
                
                
                """
                while val == nex.val:
                    nex = nex.next
                    # print(nex.val)

                cur.next = nex
                print(cur.val, nex.val,"down")
        print(cur.next.val)
        return first.next

if __name__ == "__main__":
    solution = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(3)
    n5 = ListNode(4)
    n6 = ListNode(4)
    n7 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7


    solution.deleteDuplication(n1)

"""
当时做题的一个错误思路，我知道是要用两个指针，但是单纯这样一前一后，
那么只能做到 1，2，2，3 -》 1，2，3， 而做不到1,3
因为cur到了2这里，cur就不能往后退一步了
所以正确的做法应该是，用nex,nex.next来判断，然后用cur来保留未重复的
最开始的数


还有一个细节：为什么cur会直接从2跳到5，并没有保留到4呢？
原来是因为，此时的nex.val 和 nex.next,val 都为4，虽然之前我们设了cur.next = 4
但是并没有进入到第一个判断语句中，所以这个cur.next是依旧可变的，还未确定下来的
"""