class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0: return 1

        p = 0
        n = len(nums)
        while p < n:
            num = nums[p]
            #当num没有越界（说明index合法），且nums[num-1] != num，说明需要换位置
            if 1 <= num < n and nums[num - 1] != num:
                self.swap(nums, p, num - 1)
            #当num超出[1,n)的范围，我们要跳过，不用处理
            #当nums[num-1] == num时，说明当前数字没有错，我们不用处理，可以直接跳过
            else:
                p += 1


        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

"""
https://algocasts.io/episodes/qjG0D8GK
Time: O(n), Space: O(1)
答案：
1.题目关键点，让每个index,都放上对应的数字，然后再检查对应的数字对不对，假如说不对的话，那么第一个不对的数字就是缺失的数字
  例如 应该 1  2  3
      实际 [1, 2, 0]
      放置好后：
          [1, 2, 0]
        发现 index(2) + 1 != 0,说明这个0的位置是错的，返回index+1(说明缺失了3）

主要交给while里面的那个判断来进行处理

此题可以和268题对照来看
"""