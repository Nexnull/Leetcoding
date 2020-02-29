"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
给一个binary数组，找出最长的子数组，0，1数量相等

链接：https://www.jianshu.com/p/7108226dc023
"""
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixSum = {0: -1}
        Sum = 0
        maxSubLen = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                Sum += 1
            else:
                Sum -= 1

            if Sum not in prefixSum:
                prefixSum[Sum] = i
            else:
                maxSubLen = max(maxSubLen, i - prefixSum[Sum])

        return maxSubLen

"""
思路：https://www.youtube.com/watch?v=uAGt1QoAoMU

这题，key存的是经过处理后的sum, value是index
1.其实我们可以看出这种，只要是value是index的，需要通过index相减来得到答案的，都需要吧0,-1给存进去
 这是因为，对于 从index0就满足条件的子串来说，例如
  [0,0,1,1] i = 3 
   那么 len = 3-0 = 3 是不对的
   
   但是对于非index0开始的子串，例如
   [0,0,0,0,1,1]  map= {2:1}
    len = 5 - 1 = 4, 别的数是不造城影响的，所以我们只用对key=0 进行特殊处理就好
    
2. 这题的的sum, 当遇到0的时候+1，遇到1的时候-1，当sum重新回落到一个之前字典里有的key时，说明
    碰到了一串具有相同数量的 0，1 数列

"""