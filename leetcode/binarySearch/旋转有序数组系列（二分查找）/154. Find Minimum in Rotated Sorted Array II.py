"""
Suppose an array sorted in ascending order(递增)is rotated at
some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.

Example:
Input: [2,2,2,0,1]
Output: 0

用153的代码会卡死在 [3,3,1,3] 上
Output: 3 | Expected:1
"""
class Solution(object):
    def findMin(self, nums):
        if not nums:
            return
        left = 0
        right = len(nums)-1
        while left < right: #left >= right 退出
            mid = (left + right) //2
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

"""
答案：
相比于153，只加一行代码
1.            if nums[mid] == nums[right]:
                right -= 1
原理和81一样，把分组的干扰项给去除掉再重新开始移动指针

注意，这种题去重的关键在于，第一个if 语句，是用哪两个指针进行判断的，如果那两个指针一开始出现
相同情况的话，就会出现分区错误，导致指针去错地方。81和154都一样
"""