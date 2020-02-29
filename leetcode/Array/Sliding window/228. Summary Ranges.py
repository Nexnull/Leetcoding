"""
Given a sorted integer array without duplicates, return the summary of its ranges.
Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
就是相连的数用x->y append到res里
"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if not nums or len(nums) == 0: return []
        res = []
        temp = []
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                temp.append(nums[i])
                temp.append(nums[i + 1])
            else:
                if len(temp) == 0:
                    res.append(str(nums[i]))
                else:
                    res.append(str(temp[0]) + "->" + str(temp[-1]))
                temp = []
        return res

"""
time O(n) space O(n)
答案：
1.res用来承放答案，temp用来保存每一次的连续元素
2.假如说 nums[i+1] == nums[i] + 1,就意味着他们是连续的，所以我们要把这两个数给加进去
（这里存在冗余，例如0,1,2 temp会变成[0,1,1,2]）
3.假如说是不连续的
    3.1，temp里面没有元素，例如碰到落单的一个数，那么res直接加这一个数
    3.2 temp有元素，那么我们按照它要求的格式弄好加进去就好了
"""