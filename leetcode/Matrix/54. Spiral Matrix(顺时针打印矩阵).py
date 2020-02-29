"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
"""
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if matrix is None or len(matrix) == 0 or matrix[0] is None or len(matrix[0]) == 0:
            return []

        res = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0])-1
        while True:

            for i in range(left,right+1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break

            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break

            for i in range(right,left-1,-1):
                res.append((matrix[bottom][i]))
            bottom -= 1
            if bottom < top:
                break

            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return res


if __name__ == "__main__":
    solution = Solution()
    solution.printMatrix([[1,2,3,4],
                          [5,6,7,8],
                          [11,12,13,14],
                          [15,16,17,18]])
"""
答案：
1.我们先限定出4个界限，top,bottom,left,right。他们的作用是用来遍历这个矩阵的
2.遍历顺序是顺时针方向，每遍历完一条边，准备遍历下一条边时，将要改变方向的那个变量 +1 或 -1
3. left < right , top < bottom, 每个循环结束记得检查一遍，一旦违背，说明改方向后会遍历到之前的
直接break
4.直接返回res
"""