class Solution:
    def __init__(self):
        self.count = 0

    def movingCount(self, threshold, rows, cols):
        matrix = [[1 for i in range(cols)] for j in range(rows)]
        self.findway(matrix, 0, 0, threshold)
        return self.count

    def findway(self, matrix , i , j , k):
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            return

        tmpi = list(map(int,list(str(i))))
        tmpj = list(map(int,list(str(j))))

        if sum(tmpi) + sum(tmpj) > k or matrix[i][j] != 1:
            return

        matrix[i][j] = 0
        self.count += 1
        self.findway(matrix, i+1, j ,k)
        self.findway(matrix, i-1, j, k)
        self.findway(matrix, i, j+1, k)
        self.findway(matrix, i, j-1, k)


"""
67,68都是用回溯法做，我们可以发现回溯法的规律是，在辅助函数的一开头，先设置限制条件
如果过不了限制条件，则回溯，如果过的了限制条件，则继续递归下去
"""
