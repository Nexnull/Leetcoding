from collections import Counter
from heapq import heapify, heappop


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        dic = Counter(nums)
        max_heap = [(-value, key) for key, value in dic.items()]

        heapify(max_heap)
        for i in range(k):
            res.append(heappop(max_heap)[1])
        return res


"""
Time: O(n*logn) Space: O(n)
https://www.youtube.com/watch?v=qHMcunUXSA4
1.首先我们先把nums 中元素以及元素出现的次数变成一个dic
2.然后我们创建一个heap, 把（-元素出现次数，元素）作为放入，注意这里要让元素出现的次数取负
例如 1:3,2:2 我们想取最频繁的数字，那么把[(-3,1),(-2,2)]放进heap, 最小堆的特性质， (-3,1)肯定在堆顶
这就达到了我们的目的

3.heapify过后，我们剩下的就是把堆里面的元素依次取出，这就是我们的答案了
"""