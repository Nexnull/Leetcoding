"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0: return []

        self.res = []
        self.helper(nums,[],0)
        return self.res


    def helper(self,nums,temp,cur):
        self.res.append(temp[:])

        for i in range(cur,len(nums)):
            temp.append(nums[i])
            self.helper(nums,temp,i+1)
            temp.pop(-1)

if __name__  == "__main__":
    solution = Solution()
    print(solution.subsets([1,2,3]))

"""
Time: O(2^n), Space: O(n)
答案：

注意，当for i in range(3,3)是，则不会执行这个for循环，所以我们在self.helper(nums,temp,i+1)
处理i+1 的时候不用担心our of range
"""