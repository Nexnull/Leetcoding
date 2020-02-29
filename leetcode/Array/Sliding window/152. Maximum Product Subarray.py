"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
连续子串相乘乘积为最大值
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maxproduct[i][j] i表示状态，是上一个数还是现在这个数，j表示是正数还是负数。0正1负
        if nums is None or len(nums) == 0:
            return

        maxproduct = [[0 for j in range(2)]for i in range(2)]
        maxproduct[0][0] , maxproduct[1][0] , res = nums[0] , nums[0] , nums[0]

        for i in range(1,len(nums)):
            x , y = i%2 , (i-1)%2
            maxproduct[x][0] = max(maxproduct[y][0]*nums[i] , maxproduct[y][1]*nums[i] , nums[i])
            maxproduct[x][1] = min(maxproduct[y][0]*nums[i] , maxproduct[y][1]*nums[i] , nums[i])
            res = max(res, maxproduct[x][0])
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct([2,3,-2,4]))

"""
这种有多状态的题，用二维递归最好
https://www.youtube.com/watch?v=dIU4m-K0DxU&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=48
答案：
1. maxproduct = [ 上一步[正数最大值，负数最大值]
                  这一步[正数最大值，负数最大值] ]

2.这一步的正最大值 = max( 上一步的正最大值*nums[i] , 上一步的负最大值*nums[i] , nums[i]]
  这一步的正最大值 = min( 上一步的正最大值*nums[i] , 上一步的负最大值*nums[i] , nums[i]]

3.设计巧妙的地方：
  3。1 maxproduct是个2*2 的数组，只保留上一步和当前步的状态，节省了空间
  3。2 x,y总是处以一种交替态，[x=1,y=0] ,[x=0,y=1].因此，使得y总是能储存上一步的值，而不用实际去写这个交替过程
"""
#sliding windows 做法
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0: return 0

        res , maxi , mini = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            temp = maxi
            maxi = max(num, max(temp*num,mini*num))
            mini = min(num, min(temp*num,mini*num))
            print(maxi,mini)
            if maxi > res:
                res = maxi
        return res

"""
time O(n) space O(1)
答案：
我们始终维持祝一个maxi ,mini.两个变量。当一个数字加进来的时候，就看谁更大一点
"""
















