"""
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
"""
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 and not nums2 or len(nums1) == 0 or len(nums2) == 0: return []
        heap = [(nums1[0] + nums2[y], 0, y) for y in range(len(nums2))]
        heapq.heapify(heap)
        res = []
        # 1,2  1,4  1,6
        # 7,2  7,4  7,6
        # 11,2 11,4 11,6
        # 依旧是定下第一行，然后从上往下找
        # k太大了，返回所有结果就好了
        if k > len(nums1) * len(nums2): k = len(nums1) * len(nums2)

        for i in range(k):
            val, x, y = heapq.heappop(heap)
            res.append((nums1[x], nums2[y]))
            if x + 1 < len(nums1):
                heapq.heappush(heap, (nums1[x + 1] + nums2[y], x + 1, y))
        return res

"""
https://algocasts.io/episodes/Z5mz0Qpd
这题的接发基本上和378一摸一样，唯一不同的地方在于，我们要想办法去利用两个数组去构造一个矩阵，来形成对子
且这个矩阵也要是，从左到右，从上到下递增

"""