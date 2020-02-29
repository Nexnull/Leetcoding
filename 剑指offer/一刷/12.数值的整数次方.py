class Solution:
    def Power(self, base, exponent):

        if exponent > 0:
            res = base
            for i in range(exponent-1):
                res *= base
                print(res)
        elif exponent == 0:
            return 1
        else:
            res = 1/base
            for i in range(abs(exponent)-1):
                res /= base

        return res



if __name__ == "__main__":
    solution = Solution()
    solution.Power(2,-3)