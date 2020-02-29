"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        output = [0]*length
        output[0] = 1

        for i in range(1,length):
            output[i] = output[i-1] * nums[i-1]

        right = 1
        for i in range(length-1,-1,-1):
            output[i] *= right
            right *= nums[i]

        return output

"""
https://algocasts.io/episodes/aVWyPJp2
// Time: O(n), Space: O(1)
答案：
把一个数左边的类乘算出来，把一个数的右边类乘算出来，左边类乘*右边类乘=除自己外的类乘
1.output作为输出结果，但我们先使用它来记录第一遍的从左到右的类乘
  我们已知左边第一个数的左边类乘 = 1(因为不能乘自己)
  然后遍历：
  例如 i = 3, output[3] = output[2](0*1) * nums[2]
  
2.我们用right来记录从右向左的output
  我们已知右边第一个数的右边类乘 = 1(因为不能乘自己)
  然后遍历：
  output[4] *= right[6*5] ,output[4] = [0*1*2*3]
  所以output[4]就为正确结果了
  
  right *= nums[4] right从[6*5] -> [6*5*4]

注意：
为什么空间复杂度为O（1）
"""