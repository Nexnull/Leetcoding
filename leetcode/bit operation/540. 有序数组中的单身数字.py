"""
You are given a sorted array consisting of only integers where every element
appears exactly twice, except for one element which appears exactly once.
Find this single element that appears only once.

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
"""
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high)//2
            # 在这里调整MID的位置，是为后面统一对MID处理做准备，我们统一把MID移动到两个相同数的左边INDEX
            if mid-1 >= 0 and nums[mid-1] == nums[mid]:
                mid -= 1
            elif mid+1 < len(nums) and nums[mid+1] == nums[mid]:
                mid = mid
            else:
                return nums[mid]

            # 通过判断数字左右列表的奇偶性，来判断HIGH LOW的改变
            if (mid-low) % 2 == 1:
                high = mid - 1
            else:
                low = mid + 2
        return -1

"""
答案：
方法1：一个循环，一直异或，答案为那个数。Time: O(n), Space: O(1)
方法2：二分查找  Time: O(log(n)), Space: O(1)
https://algocasts.io/episodes/dbGY42m5
1 1 2 2 3
1.mid的落位有三种情况:mid在相同数的右边，nums[mid-1] == nums[mid],这时要把mid挪到左边
                    mid在相同数的左边，nums[mid+1] == nums[mid],这时不用操作
                    mid左右无相同数，说明我们找到了，直接返回

2.假如，mid-low是奇数，说明单数在左边
        mid-low是偶数，说明单数在右边
3.我们始终要high维持在相同数的右边，所以high = mid-1
           low始终在相同数字的左边，所以low = mid + 2
"""
