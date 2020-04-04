"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input
 would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
这个题目说的是，给你一个整数数组和一个目标值，你要在数组中找到三个整数，使它们的和最接近目标值。然后返回这三个整数的和。
注意，假设给你的数组都有一个唯一解。
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return

        nums = sorted(nums)
        delta = nums[0] + nums[1] + nums[2] - target

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                diff = nums[left] + nums[right] + nums[i] - target
                if diff == 0:
                    return target
                if abs(delta) > abs(diff):
                    delta = diff
                if diff > 0:
                    right -= 1
                else:
                    left += 1

        return delta + target

"""
https://algocasts.io/episodes/k8GNv5Ge
https://www.youtube.com/watch?v=eHtHNK3Lfmw 篮子王

是3sum的一个简化版
做法其实基本一样（这里不需要对元素去重）
然后我们只需要在每次求出sum之后，对比sum与target的差值有没有更小值
有的话记录这个更小值
最后返回最小值所对应的sum
"""