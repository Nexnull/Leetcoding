"""
[[1,2,3]
[4,5,6]]

[[1,4]
 [2,5]
 [3,6]]
 要求你把一个矩阵逆时针旋转90度，不需要inplace
"""
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        cut_row = len(A)
        cut_col = len(A[0])
        res = []

        for i in range(cut_col):
            new_row = []
            for j in range(cut_row):
                new_row.append(A[j][i])
            res.append(new_row)
        return res
"""
Time space 都是O(row*col)
https://www.youtube.com/watch?v=me9ldMORnCQ
答案：
1.我们可以发现，生成的新矩阵的row,是等于原矩阵的col ,例如[1,4]是原矩阵的第一列，是新矩阵的第一行
2.所以我们的做法是，定col,变row,在原矩阵上，每列，从上往下遍历，遍历结果加进一个新列表
3.最后把新列表加进res

注意，虽然我们是定col,变row, 但是我们append()的时候，为什么要A[j][i],因为我们还是要按照
A[row][col]形式给加进res,在这种形式中，i = col, j = row,所以是A[i][j]
"""