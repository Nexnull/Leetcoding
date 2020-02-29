"""
Given a sorted array nums, remove the duplicates in-place such that each element appear
only once and return the new length.

Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        p = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[p] = nums[i]
                p += 1

        return p

"""
指针从头往后遍历一遍，T= On , 没有开辟新的空间， S = O1
答案：
1.设计两个指针，p用来记录没有重复的的元素
              i用来查找前方没有重复的元素
2.nums[i - 1] != nums[i]，说明i这个index是不重复的，所以要把i记录到p里

"""

