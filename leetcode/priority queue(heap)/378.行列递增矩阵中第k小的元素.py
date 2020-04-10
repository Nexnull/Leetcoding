import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [(matrix[0][y], 0, y) for y in range(len(matrix))]
        heapq.heapify(heap)

        for i in range(k):
            res, x, y = heapq.heappop(heap)
            if x + 1 < len(matrix):
                heapq.heappush(heap, (matrix[x + 1][y], x + 1, y))
        return res

"""
// Time: O(k*log(k)), Space: O(k)
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
利用特性，我们知道这个行列是从左向右递增，从上到下递增，所以我们可以利用堆来写这个题(所以我们是定y变x)
heapq的处理元组的时候，默认是利用第一个带数字的元素来进行排序

所以我们先把第一行的三个元素全放进heap,然后每个元素往下找，最后总能找到第k哥
"""