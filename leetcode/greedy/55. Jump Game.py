"""
55. Jump Game
Medium

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
问你能不能跳到最后
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0: return False

        n = len(nums)
        max = 0
        for i in range(n):
            if max >= n-1: return True
            if i > max: return False
            max = max(max,i+nums[i])


        return False

"""
// Time: O(n), Space: O(1)
1.我们知道，我们能跳到的最远的距离是 curindex + nums[curindex]
  所以我们只需要判断，我们在数组中找到的最大curindex + nums[curindex]
  是否 >= len(nums)-1即可
2.同时我们得保证 curindex是在maxindex的活动范围以内的
"""