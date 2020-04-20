"""
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.

"""
class Solution(object):
    def findCircleNum(self, grid):
        if not grid or len(grid) == 0:return
        n = len(grid)
        visited = [0]*n
        count = 0

        for i in range(len(visited)):
            if visited[i] == 0:
                self.dfs(grid , i , n, visited)
                count += 1
        return count

    def dfs(self,grid , curr, n ,visited):
        if visited[curr]:return
        visited[curr] = 1

        for i in range(n):
            if visited[curr][i] == 1 and visited[i] == 0:
                self.dfs(grid, i, n, visited)

"""
https://www.youtube.com/watch?v=HHiHno66j40
这题的理解方法和岛屿的数量那题有点不一样
这题不是单纯得去找图的上下左右是否连接，他有一个独特的判断方法
已知假如说有5个人，那么他们能组成一个5*5的矩阵
那我们应该创建一个长度为5的数组，里面记录每个人 是否是别人的朋友
1.A，B，C三个人，假如说扫描A的时候，发现B是A的朋友，然后我们dfsB，并没发现C是B的朋友
同时直到结束都没有发现C是A的朋友
2.那么在visited里的状态是，A,B都变成1了，C还是0，所以假如说遍历到C的时候，C也不必去看
AB了，因为前面我们已经判断过他们不是朋友了

所以这题解题的关键是dfs 那个visited 数组

"""