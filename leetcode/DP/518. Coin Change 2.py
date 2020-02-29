"""
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
要求返回出多少个不同的解
"""
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        dp = [0] * (amount + 1)
        dp[0] = 1

        for j in coins:
            for i in range(amount + 1):
                if i >= j:
                    dp[i] += dp[i - j]

        return dp[-1]

"""
dp[i] 记录了在数字i的时候，总共有多少种不同的拼凑方法

    for i in range(amount+1):
        for j in coins:
            if i >= j:
                dp[i] += dp[i-j]
    
    为什么这样写是错的,5,[1,2,5]
    dp[1] = [1]
    dp[2] = [1,1] , [2]
    dp[3] = [1,1,1] , [2,1]
    
    假如说按照上面的写法，那么 dp[3] = dp[2] + dp[1]
                    但我们发现，其实dp[2]的[2] + 1  和 dp[1] 的 [1] + 2 其实是同一种写法
                    这种写法，会出现硬币重复使用的情况（combinmation）,假如我们允许排序不同答案也是不同的话
                    那么这个写法可以
    
    所以我们最后的正确写法是，定好硬币，然后往每一个amount上进行放置，这样就可以保证不会出现硬币重复
    放置,[1,2] [2,1]这样的情况出现了 
    
"""