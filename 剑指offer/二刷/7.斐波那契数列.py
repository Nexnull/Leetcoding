"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""

class Solution:
    def Fibonacci(self, n):
        if not n:
            return

        res = [0]*(40)
        res[0] = 0
        res[1] = 1
        res[2] = 1
        res[3] = 2
        if n < 3:
            return res[n]

        for i in range(4,n+1):
            res[i] = res[i-1] + res[i-2]

        return res[n]

if __name__ == "__main__":
    solution = Solution()
    print(solution.Fibonacci(4))

"""
为了做的方便点，其实这样写空间会浪费很多
"""