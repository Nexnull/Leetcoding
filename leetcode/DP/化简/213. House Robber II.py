"""
有一排房子给你抢劫，但是有个规则就是你不能连续抢两个房子，同时你不能同时抢首尾两个house，问你最多能抢多少钱
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0: return 0
        if len(nums) <= 2: return max(nums)
        return max(self.helper(nums[:len(nums)-1]), self.helper(nums[1:]))

    # Time: O(n), Space: O(1)
    def helper(self,nums):
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
1.因为多了一个首尾房子不能同时抢的规定，其他的与上一题一样
2.所以我只要把首尾给分开成两次来求，看哪个片段比较大就好了
3.时间复杂度和空间复杂度与上题一样
"""