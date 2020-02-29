class Solution(object):
    # Time: O(m * n), Space: O(m * n)
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0: return 0

        dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

        dp[0][0] = 1 if grid[0][0] == 0 else 0
        for i in range(1, len(grid)):
            dp[i][0] = dp[i - 1][0] if grid[i][0] == 0 else 0

        for j in range(1, len(grid[0])):
            dp[0][j] = dp[0][j - 1] if grid[0][j] == 0 else 0

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) if grid[i][j] == 0 else 0

        return dp[-1][-1]


"""
https://algocasts.io/episodes/qjG08bGK
答案：
1.其实做法和62基本一样，只不过在每次更新dp值之前，我们需要去判断一下grid[i][j] = 0 ？1
如果是1的话, 那么我们给dp[i][j] = 0
如果是0的话，dp[i][j] = dp[i-1][j] + dp[i][j-1]
"""