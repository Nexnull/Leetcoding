"""
Each number in candidates may only be used once in the combination.
（candidate里的每个数都只能用一次）
Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates is None or len(candidates) == 0: return []
        self.res = []
        candidates = sorted(candidates)
        self.helper(candidates, target, [], 0)
        return self.res

    def helper(self, candidates, target, temp, cur):
        if target <  0:return
        if target == 0:
            self.res.append(temp[:])
            return

        for i in range(cur, len(candidates)):
            # 为什么这里判断重复是[i] == [i-1]呢？
            # 因为i-1 我们已经在上一个循环里用过了，我们现在想知道i能不能用
            if i > cur and candidates[i] == candidates[i - 1]:
                continue
            temp.append(candidates[i])
            self.helper(candidates, target - candidates[i], temp, i+1)
            temp.pop(-1)

"""
https://www.youtube.com/watch?v=5ybHmOt3-34
注意：
这题要保证candidates里的相同数只能用一次，但是遇到[1,2,5,2,1] t = 7这种，
即使传helper的index + 1,也避免不了重复，那要怎么办呢？

处理办法，与subset,combination那些去重复的差不多。
1.nums先排序 2.然后不让candidates[i] == candidates[i-1]

"""