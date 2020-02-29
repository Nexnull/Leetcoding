import collections

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count = collections.Counter(nums)
        return max(count.keys(), key = count.get)



if __name__ == "__main__":
    solution = Solution()
    solution.MoreThanHalfNum_Solution([1,1,1,2,3])





"""
对应leetcode169


"""