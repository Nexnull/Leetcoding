"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.(如果target不在，则返回它应该插入的地方)

You may assume no duplicates in the array.

"""
class Solution(object):
    def searchInsert(self, array, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.findright(array, target)

    def findright(self, nums, target):
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            if nums[mid] == target:
                return mid
        return left
"""
本题无法处理多个重复target的情况，因为当 nums[mid] == target时，立刻返回mid
这题非常有代表性，我们可以用这个模版来解决三个问题
1.有target时，我们能返回target(但是不能确定是返回的是哪个target,换而言之就是只能处理单target问题)
2.无target时，我们能返回非target的左界，[right]
3.无target时，我们能返回非target的右界，[left]

答案：
time: ologn space:o1
    
"""