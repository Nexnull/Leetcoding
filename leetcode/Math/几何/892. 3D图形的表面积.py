"""
Input: [[1,2],[3,4]]
Output: 34
"""
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]: area += grid[i][j] * 4 + 2
                if i: area -= min(grid[i][j], grid[i-1][j]) * 2
                if j: area -= min(grid[i][j], grid[i][j-1]) * 2
        return area

"""
Time;O(n^2) space:O(1)
https://blog.csdn.net/fuxuemingzhu/article/details/82083893#_52
这题的理解是这样的：
例如[[1,1],[1,1]]
实际上这是一个
 1 1
 1 1  这四个位置都是1的3D图形，现在我们要求它的表面积
 
怎么求，我们知道例如一个柱子， 它是有六个面组成的，上下两面，前后左右四面
例如一个高度为 4的柱子，它的表面积应该为 4*高度（前后左右四面） + 2(上下两面）

假如说有两个相邻的柱子，那么他们会有面是贴合在一起的（不算），那么不算的表面积应该是
                                                          矮的柱子的高度*2

所以在这里就是我们的算法了
"""