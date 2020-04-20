class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # 从0元开始， 到规定amount, 总共长度哦有amount+1
        dp = [0] * (amount + 1)

        # 无论你有多少硬币，到0元都只有一种情况：就是哪个都不拿
        # dp[i]表示在amount为i的时候， 最多有多少种组成方法
        dp[0] = 1

        # 存在一种无效的情况就是，例如硬币的是2，那么低于2的价钱硬币都不可以加入
        # 这就等于说对于当前面值的硬币来说，我们没必要去参与比当前面值还低的情况
        for coin in coins:
            for i in range(coin, amount + 1):
                # 因为我们是一个个硬币来进行填充
                # 所以dp[i]的值会随着硬币的更换而增加
                # 所以当前这一遍dp[i] 的值，等于上一遍dp[i]的值 + 加上这枚硬币到这一步的可能性
                dp[i] = dp[i] + dp[i - coin]

        return dp[-1]


"""
https://leetcode-cn.com/problems/coin-change-2/solution/ling-qian-dui-huan-ii-by-leetcode/
这个解析讲的很好， 这题本质上有点像跳台阶， 

当前这一遍dp[i] 的值，等于上一遍dp[i]的值 + 加上这枚硬币到这一步的可能性
"""