class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return

        slow = 0
        fast = 0

        for fast in range(len(nums)):
            # 如果fast不等于我们要移除的元素，那么就把fast填充到
            # slow里面去，然后让slow++
            # 目的是使得slow左边的都是非目标元素
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow

"""
Time: O(n), Space: O(1)
https://algocasts.io/episodes/AwmX8Jmx
"""

