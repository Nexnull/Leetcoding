"""
Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
实时判断数据流中的第k大元素
"""
import heapq


class KthLargest(object):
    # // Time: O(n * log(k))
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    # Time: O(log(k))
    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]

"""
https://algocasts.io/episodes/zbmK2MWZ
python heapq的使用方法：
创建堆（heapq是最小堆）
1。 一种是使用一个空列表，然后使用heapq.heappush()函数把值加入堆中
2。另外一种就是使用heap.heapify(list)转换列表成为堆结构

可以通过`heapq.heappop() 函数弹出堆中最小值。
如果需要删除堆中最小元素并加入一个元素，可以使用heapq.heaprepalce() 函数

堆的pop出最顶元素只需要O(1)的时间，heapfily只需要O(logk)的时间
所以综合起来说是效率很高的

答案：
1。在主函数把heap创建好，假如说heap里有超过k个数，则把超过k的数给清理出去
这样heap里留下的数就是前k大的数，最顶上的那个就是第k大的数
2。在add函数里，假如说 len(heap)< K,则说明heap里面数不够，push进去
              假如说新来的数值大于heap[0](第k大的元素）,则使用repalce,把最小的删去，把新的加入
"""