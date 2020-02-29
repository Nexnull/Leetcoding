"""
题目说明了下一行的所有值比上一行的所有值都要大
这题应该用二分查找来做
"""

class Solution(object):
    def searchMatrix(self, array, target):
        """
        :type array: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not array or len(array) == 0:
            return False

        left = 0
        right = len(array) * len(array[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            num = array[mid // len(array[0])][mid % len(array[0])]

            if target == num:
                return True
            elif target > num:
                left = mid + 1
            else:
                right = mid - 1

        return False

"""
Time: O(logn) Space:O(1)
答案：
1.由于这题说了下面一行绝对比上面一行大，所以我们可以直接把这个矩阵看作是一个有序数组
2.所以我们可以直接使用二分查找，唯一的有点不同就是，我们需要把mid转换成矩阵的格式
3.mid = (left+right)//2
  num = array[mid//len(array[0])][mid%len(array[0])]
"""