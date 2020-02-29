"""
有一排房子给你抢劫，但是有个规则就是你不能连续抢两个房子，问你最多能抢多少钱
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""
# Time: O(n), Space: O(n)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0: return 0
        if len(nums) == 1: return nums[-1]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

# Time: O(n), Space: O(1)
class Solution1(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0: return 0
        prev1 = 0
        prev2 = 0

        for num in nums:
            cur = max(prev1 , prev2 + num)
            prev2 = prev1
            prev1 = cur
        return prev1



"""
答案：
1.这题关键在于理解不能连续抢劫两个房子这个概念，
    假如说有i 和 i-1 两个房子,你选了i-1 就不能选 i，那你要如何做权衡
    选i 的隐藏含义是， 从头到i 处的和是 dp[i-2] + nums[i]
    选i-1 的隐藏含义, dp[i-1]
    所以我们要看他们两个哪个比较大，然后让dp[i] 等于两者的更大值

2.这题还可以进一步优化，因为对于dp来说，我们其实只用到了dp[i-1] 和 dp[i-2]
  于是，我们可以用两个变量来代替 dp[i-1] dp[i-2]
"""
