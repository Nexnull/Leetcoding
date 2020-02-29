"""
Given an array nums of n integers and an integer target, are there elements a, b, c,
 and d in nums such that a + b + c + d = target?
 Find all unique quadruplets（四胞胎） in the array which gives the sum of target.

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if not nums or len(nums) == 0:return res
        nums = sorted(nums)

        for p in range(len(nums) - 3):
            if p > 0 and nums[p] == nums[p-1]:continue

            for k in range(p+1,len(nums)-1):
                if k > p+1 and nums[k] == nums[k-1]: continue
                i = k + 1
                j = len(nums)-1


                while i < j:
                    s = nums[i] + nums[j] + nums[k] + nums[p]
                    if s == target:
                        res.append([nums[i], nums[j], nums[k], nums[p]])
                        while i < j and nums[i] == nums[i+1]: i += 1
                        while i < j and nums[j] == nums[j-1]: j -= 1
                        i += 1 ; j -= 1
                    elif s < target:
                        i += 1
                    else:
                        j -= 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.fourSum([-3,-2,-1,0,0,1,2,3],0))

"""
https://www.youtube.com/watch?v=YkxsyPItHeM
这题最好不要按照algocast的写法来写，因为java的for 和python 的for range的语法处理效果不同
建议按照自己的3sum的版本来写
3sum是定一个指针，移动两个指针，4sum是定两个指针，移动两个指针

注意：
每个for循环下一定要注意判断重复！！
"""