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
        if not nums:
            return False

        maxjump = 0
        terminal = len(nums) - 1

        for i in range(len(nums)):
            #我们的行动范围不能大于 最大跳跃距离，如果超过了就错了
            if i > maxjump:
                break
            # 假如说当前位置+能跳的距离 大于 最大跳跃距离， 那么我们更新最大跳跃距离
            if i + nums[i] > maxjump:
                maxjump = i + nums[i]

            # 假如我们当前位置+跳跃距离 >= 最后的位置，说明我们可以完成任务
            if i + nums[i] >= terminal:
                return True

        #假如我们所有步骤都走完了，还是没有完成任务，说明完不成任务
        return False

"""
// Time: O(n), Space: O(1)
1.我们知道，我们能跳到的最远的距离是 curindex + nums[curindex]
  所以我们只需要判断，我们在数组中找到的最大curindex + nums[curindex]
  是否 >= len(nums)-1即可
2.同时我们得保证 curindex是在maxindex的活动范围以内的
"""