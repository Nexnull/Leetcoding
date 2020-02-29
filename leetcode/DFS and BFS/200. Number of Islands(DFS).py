"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
"""
class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:return 0
        self.m = len(grid); self.n =len(grid[0])
        count = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    self.dfs(grid,i,j)
                    count += 1
        return count


    def dfs(self,grid,i,j):
        if i < 0  or j < 0 or i >= self.m or j >= self.n or grid[i][j] != "1":
            return
        grid[i][j] = "0"
        self.dfs(grid,i+1,j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

if __name__ == "__main__":
    solution = Solution()
    solution.numIslands(
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])


"""
https://www.youtube.com/watch?v=E_jxW5RqXCI&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=55

这题使用的是DFS的做法，就是所谓的鬼子扫荡式的方法：
1.进行全局遍历，当我们遍历到1的时候，我们就开始把该点的坐标放进dfs
2.dfs的终止条件是坐标越界或者是 该坐标不为1
3.成功进入dfs后我们把该点坐标改为"0"，这样就不会在dfs的时候重新扫描到自己
4.对该坐标的上下左右进行dfs扫描。直到结束，结束时说明这一整个岛也找好了
5.结束dfs递归之后，回到主函数，count+1,说明已经扫描好，且已删除了一个岛

"""