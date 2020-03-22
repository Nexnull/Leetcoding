class Solution(object):
    def subarraysDivByK(self, A, k):
        """
        :type A: List[int]
        :type k: int
        :rtype: int
        """
        if not A:
            return 0

        sum = [0 for _ in range(len(A) + 1)]
        for i in range(len(A)):
            sum[i + 1] = sum[i] + A[i]

        mod_count = [0 for _ in range(k)]
        for sec in sum:
            mod_count[(sec % k + k) % k] += 1

        res = 0
        for c in mod_count:
            res += c * (c - 1) // 2

        return res

"""
https://www.youtube.com/watch?v=pkx6SowjL7M
这题其实做法很巧妙
我们首先创建一个sum, 它代表的是从第[0-i)的子序列和， 例如 sum[1] = A[0]  sum[2] = A[0] + A[1]
所以我们创建到len+1 个，因为sum[i+1] = A[0] + A[1] + .. + A[i]

mod_count 相当于一个hashmap, 因为我们发现一个规律， sum[i],sum[j] 要是他们%k 的余数相等的话，那么他们相减产生的子序列的和
一定可以被 k整除， 例如 4 , 9, mod5 都是4， 他们相减等于5， 可以被5整除
我们要做的就是，把mod k后相等的数放到同一个位置上

假如说mod5 余4的序列有 6个，那么他们任意两两相减都可以产生被k整除的序列， 所以这里我们可以用排列组合 c*(c-1)//2 
"""