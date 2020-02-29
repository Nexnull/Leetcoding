"""
int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly.
Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""
from random import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        index = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1

                if random() <= 1.0 / count:
                    index = i
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

"""
time n space 1
https://www.youtube.com/watch?v=a9Dfp6UT2kI
https://leetcode.com/problems/random-pick-index/discuss/88081/Python-solution-with-detailed-explanation
答案：
target 对应的数只有一个的话，return 0
target 对应的数有多个的话，我们要使他们的target index返回的概率都是相同的(1/count),写法就只能这样写，其中设计数学的证明，就不去深究了
这种算法教叫做reservoir sampling
"""