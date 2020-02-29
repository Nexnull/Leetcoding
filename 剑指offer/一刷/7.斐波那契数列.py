class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            res = [0]*(n+1)
            res[0] = 0
            res[1] = 1
            res[2] = 1

            for i in range(2, n + 1):
                res[i] = res[i - 1] + res[i - 2]

        print(res,res[n])
        return res[n]

if __name__ == "__main__":
    solution = Solution()
    solution.Fibonacci(2)