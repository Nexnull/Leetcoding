"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
在algocast里有用二分查找的做法（ONlogN）
这里在算法通关40讲里面介绍的是递归的做法
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        if nums is None or len(nums) == 0:return

        res = 1
        dp = [1 for i in range(len(nums))]

        for i in range(1,len(nums)):
            for j in range(i,-1,-1):
                if dp[j] < dp[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res,dp[i])
        return res

"""
https://www.youtube.com/watch?v=bQ6Y4WQjZVY&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=50
答案：
1.这里的dp[j]就是前面已经计算过的，各位置的最长子序列数量
2.假如说我们发现[i] > [j],说明[i]可以拼接到[j]后面，所以dp[j]+1
3.为什么我们需要一个res来记录全局最大而不是用dp[-1]来表示呢
因为假如说是[1,2,3,2,1]，那么当i为最后一位的时候，它满足不了dp[j] < dp[i]，所以之前的最大值无法赋予到当前的dp[i]上，所以我们需要一个额外的res来记录最大值

"""