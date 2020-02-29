"""
摇摆序列就是一大一小一大一小这样的，求出一个最大的摇摆序列
Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].（可以跳着来找的，不一定要连续的）

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
"""
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums and len(nums) == 0:return 0

        up,down = 1,1

        for i in range(len(nums)+1):
            if nums[i+1] > nums[i]:
                up = down + 1
            elif nums[i+1] < nums[i]:
                down = up + 1
            else:
                continue

        return max(up,down)



"""
https://leetcode.com/problems/wiggle-subsequence/solution/ approach4
Time complexity : O(n)O. Only one pass over the array length.
Space complexity : O(1). Constant space is used.
答案：
规律：一个列表中 nums[i] 和 nums[i+1]的关系永远为： 1, nums[i] > nums[i+1]
                                                2, nums[i] < nums[i+1]
                                                3, nums[i] = nums[i+1]

而我们要找一个摇摆的数组，就是说一个列表里每遍历一个数，都离不开这种变化
1.我们用up, down,来储存，当前状态为up的最大摇摆数组长度，和状态为down的最大摇摆数组长度
2.使用dp,但我们不用list，而是用变量，是因为我们最多只需要用到上一个状态
3.up,down都初始化1，因为第一个数算作开始，也需要被记录

4.我们回到规律的 nums[i] 和 nums[i+1]关系
  up 的值永远取决于 down的值，因为这样递增的时候new_up 永远等于down + 1,
  但当出现小数时，down = new_up + 1 = down + 1 + 1 ,因为我们已经经历了一次up and down了，所以
  数组长度也应该要+2了


"""


