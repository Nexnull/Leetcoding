class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0 for _ in range(len(nums) + 1)]

        for i in range(1, len(nums) + 1):
            self.dp[i] = self.dp[i - 1] + nums[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j + 1] - self.dp[i]

"""
https://algocasts.io/episodes/XOp166W2
DP【I] 是表示 从[0 ~ i-1]
所以我们要求[i,j] 的话， 我们需要用 [0,j] - [0,i-1]来求出
所以用 dp[j+1] - dp[i] 就是能返回出我们想要的范围
由于是dp[j+1] 所以我们创建dp的时候，就要把数组的范围往后拓展一点，长度为len+1
dp[0] 应该为0
dp[1] 应该为num[0]
然后我们就可以推出我们的递推式了
"""