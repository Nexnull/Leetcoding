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

        uf = UnionFind(grid)
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        m, n = len(grid) , len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                for d in directions:
                    nr , nc = i + d[0], j + d[1]
                    if nr >= 0 and nc >= 0 and nr < m and nc < n \
                            and grid[nr][nc] == "1":
                        uf.union(i*n + j, nr*n + nc)
                        #i*n + j是当前岛屿， nr*n +nc是相邻岛屿
        return uf.count

class UnionFind(object):
    def __init__(self,grid):
        m, n = len(grid) , len(grid[0])
        self.count = 0
        self.parents = [-1]*(n*m)
        self.rank = [0]*(n*m)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # 初始化每个node,把自己的parent指向自己，同时统计1的个数
                    self.parents[i*n + j] = i*n + j
                    self.count += 1

    # 从i 开始向上找最父亲节点，父亲节点的特性是 指向自己
    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parents[rooty] = rootx
            elif self.rank[rooty] > self.rank[rootx]:
                self.parents[rootx] = rooty
            else:
                self.parents[rooty] = rootx
                self.rank[rootx] += 1
            # 因为每块岛屿都有一个自己的父亲（自己），假如说相邻岛屿合并了，代表父亲数量的count -= 1
            self.count -= 1

"""
https://www.youtube.com/watch?v=E_jxW5RqXCI&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=55
这个是用并查集合的做法来写的
1.我们需要初始化所有的1，让他们的父亲都是自己
2。然后我们把相邻的岛屿都合并（上下左右），在并查集里面，我们要把相邻岛屿父亲都指向
同一个父亲
3。最后我们看看还剩下多少个父亲，就说明有几个不相邻的岛屿

"""