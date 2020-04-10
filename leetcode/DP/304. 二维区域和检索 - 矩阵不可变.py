class NumMatrix(object):

    # 这个函数是让我们先求出所有矩阵的前缀和
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        self.dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.dp[i][j] = self.dp[i - 1][j] + self.dp[i][j - 1] + \
                                matrix[i - 1][j - 1] - self.dp[i - 1][j - 1]

    # 这个函数是在我们求完前缀和以后，然后利用前缀和来进行求值
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] \
               - self.dp[row1][col2 + 1] + self.dp[row1][col1]

"""
https://algocasts.io/episodes/VBpLE6WD
https://leetcode-cn.com/problems/range-sum-query-2d-immutable/solution/huan-cun-dong-tai-gui-hua-python3-by-zhu_shi_fu-2/
看图来的直接点吧


"""