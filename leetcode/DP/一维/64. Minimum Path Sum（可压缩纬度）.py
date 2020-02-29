

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid or len(grid) == 0: return 0

        m = len(grid)
        n = len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]


"""
https://algocasts.io/episodes/AEpoAMmQ
  // Time: O(m*n), Space: O(m*n)
答案：
1.这题与62题很相似，是一个矩阵，但是这里我们多了一个grad数组
2.dp是用来盛放路径和的数组
3.首先我们把只能由一个方向走到的点给附值，就是那两个for循环
4.因为我们要找到路径和最小的路 之和。所以我们这里的递推式子是 
    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
  因为[i][j] 这个点我们可以从上往下走到达和从左往右走到达，所以取min
  然后还要加上这一步[i][j]的和
"""