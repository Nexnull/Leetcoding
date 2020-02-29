"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[[1,1,2],
  [1,2,1],
  [2,1,1]]
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) == 0: return []
        self.res = []
        self.visited = [False] * len(nums)
        self.helper(sorted(nums), [])
        return self.res

    def helper(self, nums, temp):
        if len(temp) == len(nums):
            self.res.append(temp[:])

        for i in range(len(nums)):
            if self.visited[i]: continue
            if i > 0 and nums[i] == nums[i - 1] and self.visited[i - 1]:
                continue

            self.visited[i] = True
            temp.append(nums[i])
            self.helper(nums, temp)
            self.visited[i] = False
            temp.pop(-1)

"""
相比于permutation, 唯一的区别就是多了一个去重的处理
1. nums = sorted(nums) , 排序好了才可以去重
2. if i > 0 and nums[i] == nums[i - 1] and self.visited[i - 1]
   采用了全局去重，i > 0, 于此同时，我们要注意 self.visited[i-1] == False
   因为去除 i的重，要保证i-1已经在 答案列表里面了 

"""