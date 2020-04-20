class Solution(object):
    # 防止数字溢出
    def convert(self, x):
        if x >= 2 ** 31:
            x -= 2 ** 32
        return x

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for bit in range(32):
            cur_sum = 0

            for num in nums:
                # 统计当前bit上，有多少个1
                cur_sum += (num >> bit) & 1

            if cur_sum % 3 == 1:
                # 假如说当前bit sum mod=1
                # 这说明了出现一次的数字在当前bit上不为0
                # 我们这样拼接32个bit, 就能还原出只出现一次的数字
                # 我们把mod = 1的位，全部or到res上去
                res |= (1 << bit)

        return self.convert(res)


"""
https://algocasts.io/episodes/qjG0eXpK
Time: O(n), Space: O(1)
"""