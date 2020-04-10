class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            else:
                left += 1
        return []

"""
Time: O(n), Space: O(1)
https://algocasts.io/episodes/6emEjGVr
答案：
因为是排序的，所以直接用双指针来做。时间空间效率最高
"""