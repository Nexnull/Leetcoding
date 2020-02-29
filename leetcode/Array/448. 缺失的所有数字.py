"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
在这个长度为8的数组，缺少了5，6这两个数
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums and len(nums) == 0: return []
        res = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res

"""
Time: O(n), Space: O(1)
https://algocasts.io/episodes/dlWb1kpv
答案：
这题算41题的入门版
1. 关键思路还是 nums[num - 1] ?= num
"""