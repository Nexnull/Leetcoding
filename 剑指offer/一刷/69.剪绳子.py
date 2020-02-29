class Solution:
    def cutRope(self, number):

        if(number == 0):return 0
        if (number == 1): return 0
        if (number == 2): return 1
        if (number == 3): return 2

        dp = [0]*(number+1)

        dp[0] = 0
        dp[1] = 0
        dp[2] = 2
        dp[3] = 3
        for i in range(4,number+1):
            max = 0
            for j in range(1,4):
                if max <(dp[j]*dp[i-j]):



                    max = dp[j]*dp[i-j]
                    print(max, dp[j], dp[i - j],i)

            dp[i] = max
        print(dp)
        return dp[number]


if __name__ == "__main__":
    solution = Solution()
    print(solution.cutRope(10))





























"""
需要先理解题目的意思
给你一段长number的绳子，至于你要把它裁成几段，那就是你自己的事，只要是最后乘积最大就行了
毫无想法，这个题的可变性太大了，无法限定范围


答案：
1。递归算法：
已知道绳子长度i, 在i小于4的时候，最高为2*2
               而在i大于4之后，则可以分成 n*2 * m*3, 因为例如6 < 2*4 < 3*3
因此我们可以知道，当我们用2，3去分解来乘的时候，能达到最大解
同时使用越多3就有越多最大解
所以应对这种情况，我们可以使用递归， 一根绳子长为i,设2或3 为j, 那么i-j这个长度的绳子之前已经有过最优解了，所以直接乘上
就好了

然后递归列表的前几位是为了方便后面计算而设置的，其小于4的值我们在一开始就已经写好了可以等待返回


2。贪心算法
已知3越多，则乘积越大 3*3 > 2*2*2
则我们先把最多能分成几个三给找出来
然后再把余下最多能分成几个二找出来
最后互乘
这个解法就比较简单粗暴
"""

class Solution:
    def cutRope(self, number):

        if(number == 0):return 0
        if (number == 1): return 0
        if (number == 2): return 1
        if (number == 3): return 2

        time_of_3 = number / 3

        # 当绳子最后为4是，这时候分成 2 2而不是3 1，因为 2 2 大一点
        if number - time_of_3*3 == 1:
            time_of_3 -= 1

        time_of_2 = (number - time_of_3*3) / 2
        return pow(2,time_of_2)*pow(3,time_of_3)