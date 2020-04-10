"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13.
"""
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])

        l = matrix[0][0]
        r = matrix[-1][-1] + 1

        while l < r:
            count = 0
            mid = (l+r)//2
            # 我们要找有多少个元素小于或等于mid
            count = self.get_count(matrix, mid, m)
            if count < k:
                l = mid + 1
            else:
                r = mid

        return l

        # 求count是，从左下往右上遍历，O(N)
    def get_count(self, matrix, target, m):
        i = 0
        j = m - 1
        counter = 0
        while j >= 0 and i < m:
            # !!! 小于等于，必须包含相等，即便等于目标值的数量
            if matrix[i][j] <= target:
                counter += j + 1
                #是按一列列来计算的,算完一列移动到下一列
                i += 1
            else:
                j -= 1
        return counter

"""
https://www.youtube.com/watch?v=1VkP3Ndu1C4&t=311s
"""