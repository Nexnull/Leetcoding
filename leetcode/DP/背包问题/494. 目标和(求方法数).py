import sys


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # sum_表示偏移量，因为有可能产生 j - nums[i]有可能是负数下标
        sum_ = 0
        for num in nums:
            sum_ += num

        # 假如说我们需要得到的和， 大于数组里所有元素的和，那么说明根本不存在一种符号能
        # 得到这个结果
        if abs(S) > abs(sum_):
            return 0

        # 我们把dp的(0,0)中心坐标放在 sum 上， 这样使得 j + nums[i], j - nums[i]不会越界
        total = sum_ * 2 + 1
        dp = [[0 for j in range(total)] for i in range(len(nums))]

        # 当nums[0] == 0 的时候，sum_ + nums[0] == sum_ - nums[0]
        # 要是单纯附值的话那可能不行， 因为这个时候会省略附值一个1， 所以我们要对这种情况处理
        if nums[0] == 0:
            dp[0][sum_] = 2
        else:
            dp[0][sum_ + nums[0]] = 1
            dp[0][sum_ - nums[0]] = 1

        for i in range(1, len(nums)):
            for j in range(total):
                # index out of range的数字我们按照0种可能性来进行处理
                l = dp[i - 1][j - nums[i]] if 0 <= j - nums[i] < total else 0
                r = dp[i - 1][j + nums[i]] if 0 <= j + nums[i] < total else 0

                # 递推式子 dp[i][j] = dp[i-1][j - nums[i]] + dp[i-1][j + nums[i]]
                dp[i][j] = l + r

        return dp[-1][sum_ + S]

"""
https://leetcode-cn.com/problems/target-sum/solution/dong-tai-gui-hua-si-kao-quan-guo-cheng-by-keepal/
"""