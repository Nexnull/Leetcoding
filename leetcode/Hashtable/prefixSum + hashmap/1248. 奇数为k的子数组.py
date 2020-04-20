class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 这里定义的是 key是 有多少个奇数， value是有key个奇数的子序列有多少
        # 2 2 2 2
        # 那么遍历到最后形成的是{0:4}, 因为有0个奇数的子数组有四个
        prefix = {}

        # 初始化，表示当没有元素的时候，存在一个包含0个奇数的子数组
        prefix[0] = 1

        odd = 0
        res = 0

        for i in range(len(nums)):
            #
            if nums[i] % 2 == 1:
                odd += 1

            # 当odd大于K时， 说明存在一段子序列[i...j], 里面包含了k个奇数，所以我们要把这一段子序列的所有可能性给加进res里
            # 这一段子序列的所有可能性 = prefix[i]的所有可能性
            # [1] [1,2] [1,2,2] [1,2,2,2] 他们都是奇数数量是1，但可能的子数组是4
            if odd >= k:
                res += prefix[odd - k]

            # 因为用了defaultdict, 所以假如说 key不存在时，他会默认0且加一
            # 若key存在时， 说明[0...i] 中有odd个奇数的数组又增加一个
            prefix[odd] = prefix.get(odd, 0) + 1

        return res

"""
答案2
https://leetcode-cn.com/problems/count-number-of-nice-subarrays/solution/tong-ji-you-mei-zi-shu-zu-by-leetcode-solution/
"""