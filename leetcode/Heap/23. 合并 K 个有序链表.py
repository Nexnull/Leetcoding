# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import heapreplace,heapify,heappop
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        res = cur = ListNode(0)

        min_heap = [(n.val,n) for n in lists if n]
        heapify(min_heap)

        while min_heap:
            value, n = min_heap[0]
            if n.next is None:
                heappop(min_heap)
            else:
                heapreplace(min_heap,(n.next.val , n.next))

            cur.next = n
            cur = cur.next
        return res.next

"""
 // Time: O(n*log(k)), Space: O(k)
https://leetcode.com/problems/merge-k-sorted-lists/discuss/10513/108ms-python-solution-with-heapq-and-avoid-changing-heap-size
https://algocasts.io/episodes/RVmVkkGQ
1.我们先创建创建两个指针指向一个新的node,一个用来记录，一个用来return 答案
2.然后我们创建mini_heap, 用的是 (n.val, n) 这样的顺序, 因为这个heaplify就会按照node.val来进行排序
3. heapify
4. 我们每次都把min_heap的堆顶元素取出，因为它是当前三个node里面最小的
5. 假如说n.next == None,说明这个链表已经走到最后了，没有利用价值，就要把它给t了
6. 假如n.next还有的话，那我们就要把n.next给搞进heap，把n搞出去
7. 最后完成的时候就是要把答案链表给串起来

"""