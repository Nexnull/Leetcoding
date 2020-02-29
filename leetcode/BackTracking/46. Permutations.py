"""
Given a collection of distinct integers, return all possible permutations.
Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) == 0: return []
        self.res = []
        self.visited = [False]*len(nums)
        self.helper(nums,[])
        return self.res

    def helper(self,nums,temp):
        if len(temp) == len(nums):
            self.res.append(temp[:])

        for i in range(len(nums)):
            if self.visited[i]:
                continue

            self.visited[i] = True
            temp.append(nums[i])
            self.helper(nums,temp)
            self.visited[i] = False
            temp.pop(-1)

"""
https://www.youtube.com/watch?v=zIY2BWdsbFs
Time: O(n*n!), Space: O(n)
答案：
例子num = [1,2,3]
1.我们把nums的数字一个个放进去尝试，第一放1, 然后尝试1,(1,2,3),发现1在里面了，所以只有可能[1,2],[1,3]
2.[1,2]再尝试(1,2,3),发现只有3可以，所以生成123
3.[1,3]尝试（1,2,3),发现只有2可以，所以生成132
4.123,132完成后，把最后一位给pop（）掉，变成12,13,发现还是执行完了，再把最后一位给pop，变成1，最后1被pop()
5.开始执行以2为首的数

注意：
1.append()的时候, temp[:],这是temp的深拷贝，即是说，对temp进行任何操作都不会影响到到temp[:]
假如说我们res.append(temp),那么后面清空temp会影响到res的结果
"""
