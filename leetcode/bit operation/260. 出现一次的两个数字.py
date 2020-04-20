class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        mark = 1

        # 先把两个只出现一次的数字异或到xor上
        for num in nums:
            xor ^= num

        # 找到第一个分叉的点，mark表示分叉点在第几位
        # 分叉点可以表示为 0 1， 两个只出现一次的数字在这里肯定是分为 0 1
        while (xor & mark) == 0:
            mark <<= 1

        # 我们把mark位上0的分一组，mark位上为1的分一组
        # 这样我们就可以测出两边的不用了
        x = 0
        y = 0
        # 我们需要找到
        for num in nums:
            if (num & mark) == 0:
                x ^= num
            else:
                y ^= num

        return [x, y]

"""
https://algocasts.io/episodes/yRp366G4
Time: O(n), Space: O(1)
"""