class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[p - 2]:
                nums[p] = nums[i]
                p += 1

        return p

"""
https://www.youtube.com/watch?v=JimP_qCjb0Q
p-2，p-1 这两个元素是允许重复的
但p 是不允许重复的
所以我们每一次就看i ==? p-2, 假如说不等的话，说明p-2.p-1 与 p不相同，于是我们可以把i放到p的位置上
"""