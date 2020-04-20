"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute ！！！the fewest number of coins！！！ that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
找出最少需要多少硬币才能拼成amount
"""
import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if coins is None or len(coins) == 0 or amount is None:
            return -1

        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        if dp[amount] > amount:
            return -1
        return dp[amount]


"""
https://www.youtube.com/watch?v=EQzIfxOx8N0&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=51
这个问题和爬楼梯问题有点像
amount就是目标台阶数
coins就是我们一次可以迈多少步
dp就是在每一个数上，我们最少可以迈多少步

答案： time O^2
递推式子: dp[i] = min(dp[i] , dp[i - coin] + 1 ) 
1.由于我们要找能拼成面值为amount的数最少有几个，用的是递归，所以也要保证[amount]有位置
2.我们把dp的每个数初始化成amount+1 就是为了在最后判断到底这个数能不能用硬币拼起来
拼不起来就返回-1
3.dp[0]设为0是因为，钱数为0的时候不可能有方案可以拼(!!!最重要的一步)，这个影响到后面的所有递推结果
4.注意i 是从1开始遍历，因为0没有遍历的必要，当然这一步有没有问题不大
5.当硬币值 < amount值我们才可以递归（常理）
6.最后return 处理一下
"""