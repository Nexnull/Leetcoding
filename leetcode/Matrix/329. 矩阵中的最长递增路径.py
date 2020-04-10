
class Solution(object):
    def __init__(self):
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or len(matrix) == 0: return 0

        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        maxlen = 1

        for i in range(m):
            for j in range(n):
                temp_len = self.dfs(matrix, i, j, m, n, dp)
                if temp_len > maxlen:
                    maxlen = temp_len
        return maxlen

    def dfs(self, matrix, i, j, m, n, dp):

        if dp[i][j] != 0:
            return dp[i][j]

        maxlen = 1

        for dir in self.dirs:
            x = i + dir[0]
            y = j + dir[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            length = 1 + self.dfs(matrix, x, y, m, n, dp)
            maxlen = max(maxlen, length)

        dp[i][j] = maxlen
        return maxlen




if __name__ == "__main__":
    solution = Solution()
    num = [[1,2]]
    print(solution.longestIncreasingPath(num))

"""
解法1：https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78308/15ms-Concise-Java-Solution
解法2：https://www.youtube.com/watch?v=yZGpDJlcxRA
答案：
感觉说起来很简单，但是想要写对是有点难度的
1.创建一个和矩阵规模一样的dp数组，用来记录每个点所能找到的最长递增字串的长度
2.然后我们遍历矩阵的每一个点，从每个点出发去寻找最长递增字串
3.在dfs()里，假如说我们碰到了已经被找过的点，那么直接返回那个点的dp值
            假如说碰到没被找过的点，那么从这个点出发继续dfs

"""