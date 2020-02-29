"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: [1,2,2]
Output:
[[2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0: return []

        self.res = []
        nums = sorted(nums)
        self.helper(nums, [], 0)
        return self.res

    def helper(self, nums, temp, cur):
        self.res.append(temp[:])

        for i in range(cur, len(nums)):
            if i > cur and nums[i] == nums[i-1]: continue
            temp.append(nums[i])
            self.helper(nums, temp, i + 1)
            temp.pop(-1)



if __name__ == "__main__":
    solution = Solution()
    print(solution.subsetsWithDup([1, 2, 2]))

"""
https://www.youtube.com/watch?v=FTgi4CT7U2o
注意：
如何去重：
1. 在这题里面，我们去重的目的是，不让相同的数字做开头多次
   这就意味着：允许相同数字做一次开头，但是不会允许相同数字做第二次开头
2. 这题是dfs,遍历顺序是往深遍历的，但是从我们不允许相同数字开头的情况下来讲，每一个for循环，就是在确定开头
3. 特殊情况，例如[1,2,2],假如说现在到了[1,2]，然后下次的[cur] = 2,按理说应该输出[1,2,2].
       假如这里我们令 if i > 0 and nums[i] == nums[i-1]:, 那么最后一个2就无法被加进答案
       因为i > 0,是有点无限制的感觉，只要是重复都立刻剔除
   
       但假如说我们改成 i > cur and nums[i] == nums[i-1]。我们就能保住那个2，因为那个2并不是开头
       

                   1 2 2
            1           2        2(no)
       12     12(no)    22  
    122

    我们看这个表就可以知道，这题的去重是同层去重，而不是无限制去重（全部都去重）

    combination sum2 与这题的去重方法一样，都是同层去重

注意nums得先排序一遍再调用helper,要不然无法判断去重

"""