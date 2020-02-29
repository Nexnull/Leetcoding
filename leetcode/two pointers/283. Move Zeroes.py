"""
Given an array nums, write a function to move all 0's to the end of it while maintaining
the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0: return []

        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                fast, slow = fast+1, slow+1
        return nums

if __name__ == "__main__":
    solution = Solution()
    print(solution.moveZeroes([0,1,2,3,4,5,1]))
"""
Time: O(n), Space: O(1)
答案：双指针
1.fast是用于查找的指针，slow是用来换位的指针
2.fast永远是快于slow
  fast把非0数与slow互换，于是slow当前位置一定是非0，所以slow可以放心++，
                           fast当前位置 1。0，跳过
                                       2. 非0，交给slow去处理
                                       
3.要这样想，slow后面都是非0数，这等于是一个递推式子 1,2,3,0,0,1
                                                     s   f
最后一换，肯定也是达到目的。
"""