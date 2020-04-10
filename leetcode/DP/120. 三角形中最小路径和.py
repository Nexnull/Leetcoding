"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]

"""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle == None:
            return 0

        res = triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                res[j] = triangle[i][j] + min(res[j],res[j+1])
        return res[0]

"""
答案：
1.回溯法，time O 2^n(n个node,每个node的左右都探索)
每一条路都探索一遍，探索完成以后记录结果，返回最小值
但是这样时间复杂度很高，因为存在重复探索的情况

2。贪心，不可取，因为有可能选择的路前大后小

3。DP
    可以用二维的数组储存，但是我们用一个数组来储存，叫状态压缩
    time O(n*m)
  1.让res 等于triangle的最后一行
  2.从倒数第二行往上递推，每次向上递推都取 min(正下方，和正下方右边的node) + 本身的node.val
  3.return res[0]
  
  

"""