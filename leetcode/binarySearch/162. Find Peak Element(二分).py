"""
A peak element is an element that is greater than its neighbors.（关键）
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.
[1,2,1,3,5,6,4] output=1 or 5
[5,5,5] not answer
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1

        while left < right-1:
            mid = (left + right)// 2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid

            if nums[mid+1] > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return left if nums[left] > nums[right] else right
"""
O(logn) O(1)
https://www.youtube.com/watch?v=NJBBJimXggo
https://leetcode.com/problems/find-peak-element/discuss/50259/My-clean-and-readable-python-solution
二分查找左闭右闭写法

二分查找指针移动的趋势是，指针向大的那边走
(length >= 3)
0.我们要保证进入while循环的len(nums) >= 3, 所以我们当length,[left,right] = 2时
我们就要退出for循环了，或者说，当length,[left,right] = 2时，我们就不应该进入while循环
1.假如说 3 5 3,  mid > mid-1 , mid > mid+1, 说明mid就是peak,返回
2.假如说 [mid+1] > mid: mid->mid+1 是在增加的，说明peak在[mid+1，...]
3.假如说 [mid+1] <= mid: 说明mid->mid+1 是在见效的，说明peak在[...,mid-1]
  为什么不用考虑mid是不是peak,因为我们已经经过1的判断了，所以这里的区间不用把mid给包括进去

(length <= 2)
4.一开始就没进while循环，把列表中最大的数的index 给return 出去
5.进了while循环，发现nums是个递增/递减数组，然后指针总是朝向value大的地方移动，所以最后能返回出
这个数组最大的数
"""