class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        zeros, l, res = 0, 0, 0
        for r in range(len(A)):

            if A[r] == 0:
                zeros += 1

            while zeros > K:
                if A[l] == 0:
                    zeros -= 1
                l += 1

            if r - l + 1 > res:
                res = r - l + 1
        return res

"""
https://blog.csdn.net/qq_17550379/article/details/88101343
其实这题就是等于让你求，求一个包括K个0的最长子序列
所以我们需要维持一个双指针
右边指针，指向0的话，就说明窗口里多一个0,zeros+1
左边指针指向0，要往右走，说明窗口里要少一个0。 zeros-1

"""