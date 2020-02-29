class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums and len(nums) == 0:
            return 0

        nums = sorted(nums)
        maxLen = 0
        p = 0

        while p < len(nums):
            Len = 1
            while p < len(nums) - 1:
                if nums[p + 1] - nums[p] > 1:
                    break
                if nums[p + 1] - nums[p] == 1:
                    Len += 1
                p += 1

            if Len > maxLen: maxLen = Len
            p += 1
        return maxLen


    def longestConsecutiveSet(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums and len(nums) == 0:
            return 0

        sets = set(nums)
        maxLen = 0
        p = 0

        while p < len(nums) and len(sets) != 0:

            num = sets.pop()
            low = num - 1
            high = num + 1

            while low in sets:
                sets.remove(low)
                low -= 1
            while high in sets:
                sets.remove(high)
                high += 1

            maxLen = max(maxLen, high - low - 1)
            p += 1

        return maxLen

"""
https://algocasts.io/episodes/AEpo1MmQ

"""