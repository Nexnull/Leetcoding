
"""
一般我们说第K小，第K大，前K个最小，前K个最大
这就是提示我们使用堆
假如说是一个元组的构成的heap，那么heap会按照元组的第一个元素来进行排序
"""



import heapq
def function():

    # heapify是列表a按照最小堆的顺序排序
    # heappop(heaplist) 使得pop出列表a最小的元素
    a = [3,4,5,1,2,6]
    heapq.heapify(a)
    print(heapq)
    print(a)
    print(heapq.heappop(a))
    print("----------")

    # heapreplace(heaplist,item) 弹出最小元素，压入指定元素（a的容量不变）
    a = [3,4,5,1,2,6]
    heapq.heapify(a)
    heapq.heapreplace(a,5)
    print(a)
    print(heapq.heappop(a))
    print("----------")

    # heappush(heaplist,item) 增大heap(heaplist)的容量,把push的元素加进去
    a = [3, 4, 5, 1, 2, 6]
    heapq.heapify(a)
    heapq.heappush(a, 0)
    print(a)
    print(heapq.heappop(a))


if __name__ == "__main__":
    function()

"""
https://www.jianshu.com/p/cae1aa02d97f
heapq.heappush(heap, item)：将 item 元素加入堆。    O（logk)
heapq.heappop(heap)：将堆中最小元素弹出。
heapq.heapify(heap)：将堆属性应用到列表上。在出现(key,value)时，它的heapify是按照key的值来排的O(logk)
heapq.heapreplace(heap, x)：将堆中最小元素弹出，并将元素x入堆(无论x是小于最小值还是大于最大值，都执行)
heapq.merge(*iterables, key=None, reverse=False)：
将多个有序的堆合并成一个大的有序堆，然后再输出

heapq.heappushpop(heap, item)：将item 入堆，然后弹出并返回堆中最小的元素。
heapq.nlargest(n, iterable, key=None)：返回堆中最大的 n 个元素。
heapq.nsmallest(n, iterable, key=None)：返回堆中最小的 n 个元素
"""