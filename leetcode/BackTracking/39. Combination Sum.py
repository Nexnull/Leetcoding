"""
The same repeated number may be chosen from candidates unlimited number of times.
（可重复使用使用candidate里的数）
Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates is None or len(candidates) == 0: return []
        self.res = []
        self.helper(candidates, target, [], 0)
        return self.res

    def helper(self, candidates, target, temp, cur):
        if target < 0: return
        if target == 0:
            self.res.append(temp[:])
            return

        for i in range(cur, len(candidates)):
            if candidates[i] <= target:
                temp.append(candidates[i])
                self.helper(candidates, target - candidates[i], temp, i)
                temp.pop(-1)

"""
https://www.youtube.com/watch?v=zIY2BWdsbFs
eg[2,3,6,7] t = 7
注意：这里的target为什么减完后不需要还原？
因为对于同一个for 循环来说，每个target都是相同的，意思就是说，假如说candidate[i] = 2,那么就是从2开始往下找
                                            同样的，对于candiditaes[i] = 7来说，也是从7开始往下找，所以
                                            大家机会都一样，不需要对target进行任何操作
                                            
1.组合，意味着无序，假如说，[1,1,3],[3,1,1],[1,3,1]对于组合来说是相同的，所以我们只用传里面的一个答案就好
  但对于permutation 是不同的。所以permutation 要用一个used来记载当前使用着哪个元素。
  所以对待组合题目，我们传递helper的时候，应该是传递candidates的index，使得之前已经被传递过的数，不应该被
  再次传递
2.同时因为这题是允许重复的，所以我们传参数，不需要传i+1, 只用传i就好了

剪枝：
1. if target < 0: return . 因为已经不能满足题目条件了，所以我们遇到这种情况直接return 
2. 我在helper的 for里面增加了剪枝，只要有可能出现 target - candidate[i] < 0,的直接省略

"""