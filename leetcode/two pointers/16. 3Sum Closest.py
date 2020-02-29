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
import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None and len(nums) == 0:return 0
        nums = sorted(nums)
        res = sys.maxsize

        def threeSumClosest(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            if nums is None and len(nums) == 0: return 0
            nums = sorted(nums)
            res = 0
            mini = sys.maxsize

            for k in range(len(nums) - 2):
                i = k + 1
                j = len(nums) - 1

                while i < j:
                    s = nums[k] + nums[i] + nums[j]
                    if s == target:return s
                    if abs(target - s) < mini:
                        mini = abs(target - s)
                        res = s
                    if i < j and s < target:i += 1
                    elif i < j and s > target:j -= 1

            return res

"""
https://algocasts.io/episodes/k8GNv5Ge
是3sum的一个简化版
做法其实基本一样（这里不需要对元素去重）
然后我们只需要在每次求出sum之后，对比sum与target的差值有没有更小值
有的话记录这个更小值
最后返回最小值所对应的sum
"""