"""
Given an integer array with all positive numbers and no duplicates,
find the number of possible combinations that add up to a positive integer target.
Example:
nums = [1, 2, 3]
target = 4
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
"""
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target == 0 or len(nums) == 0: return 0

        dp = [0]*(target+1)
        dp[0] = 1

        for i in range(1,target+1):
            for num in nums:
                if num <= i:#保证i-num >= 0
                    dp[i] += dp[i - num]

        return dp[-1]


"""
这题用回溯法会超时

https://www.youtube.com/watch?v=yNq7JFd7sHE&t=81s
Where n is length of nums and m is target,
Time complexity: O(nm)
Space complexity: O(m)
"""