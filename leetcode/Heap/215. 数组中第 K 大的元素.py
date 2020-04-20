import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minheap = []

        for num in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, num)
            else:
                if num > minheap[0]:
                    heapq.heapreplace(minheap, num)

        return minheap[0]


"""
https://algocasts.io/episodes/vkmelbWb
Time: O(n*log(k)), Space: O(k)
答案：
1.我们建立和维护一个最小堆
2.当最小堆的大小小于 k时，我们就不断往最小堆里面插入数字
3.当最小堆的大小大于 k时，且num > 堆顶元素， 说明到目前位置这个num 是前k大的
  我们就要开始用 heapreplace去进行替换
4. 最后我们返回heap的堆顶元素，那个就是第k大的元素


"""