class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total = sum(nums)

        # 不能正好被分割， 所以是False
        if total % 2 == 1:
            return False

        total = total // 2

        dp = [[False for j in range(total + 1)] for i in range(len(nums))]

        # 第 0 行，第 1 个数只能让容积为它自己的背包恰好装满
        if nums[0] <= total:
            dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            for j in range(1, total + 1):

                # 说明当前num刚好能填满背包
                if nums[i] == j:
                    dp[i][j] = True
                    continue

                # 当前num不能仅靠自己填满背包，那我们要看看
                # [0- i-1]个数可不可以填满背包
                # 加上当前这个数，能不能填满背包
                if nums[i] < j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

        return dp[-1][total]


"""
时间复杂度：O(NC)：这里 N是数组元素的个数, C 是数组元素的和的一半。
空间复杂度：O(NC)
https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-xiang-jie-zhen-dui-ben-ti-de-yo/

如何理解本题的状态转移方程：
dp[i][j]表示从数组的 [0, i] 这个子区间内挑选一些正整数，每个数只能用一次，使得这些数的和恰好等于 j
dp[i][j]表示，对于前 i 个物品，当前背包的容量为j时，若 x 为 true，则说明可以恰好将背包装满，若 x 为 false，则说明不能恰好将背包装满。
比如说，如果 dp[4][9] = true，其含义为：对于容量为 9 的背包，若只是用前 4 个物品，可以有一种方法把背包恰好装满。

状态转移方程：
1、不选择 nums[i]，如果在 [0, i - 1] 这个子区间内已经有一部分元素，使得它们的和为 j ，那么 dp[i][j] = true；
2、选择 nums[i]，如果在 [0, i - 1] 这个子区间内就得找到一部分元素，使得它们的和为 j - nums[i]。

"""