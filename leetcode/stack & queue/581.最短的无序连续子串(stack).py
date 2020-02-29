"""
给你一个应当是从小到大排列的数组（允许元素相等），但里面有一部分连续的子串是混乱的
让你求，
"""
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        left = len(nums)
        right = 0

        for i in range(len(nums)):
            while len(stack) > 0 and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)

        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)

        if right - left > 0: return right - left + 1
        return 0

"""
https://www.youtube.com/watch?v=ExaJeXua-h0
有两种做法
1.排序法，我们先做一个原数组的deepcopy,然后把它给sort,然后用两个指针
分别从两个数组的头尾向中间扫，找到两个第一个出现非递增的元素，right-left+1
时间复杂度高一点

2.stack
1.从头到尾时，我们把满足递增的index加进stack,当遇到非递增的，就pop出来
  然后left一直取min index
2.从尾巴到头，我们把满足递减（反过来了）的index加进stack,遇到非递减的，就pop出来
  然后right一直取max index
3. right- left + 1
"""