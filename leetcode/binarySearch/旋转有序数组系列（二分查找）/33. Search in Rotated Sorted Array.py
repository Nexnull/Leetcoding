"""
Suppose an array sorted in ascending order is rotated
at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0:return -1

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid

            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    #target >= num[mid]（还在本区间内）
                    # target < nums[left], 则说明target不在本区间内，需要left + 1来使mid
                    # 进入到另外一个区间
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

"""
https://algocasts.io/episodes/6emEOjpV
time O(logn) space O(1)
答案：
主要模式还是把一个列表分成两块，大递增一块，小递增一块，我们根据[mid]和[left]的关系，来锁定一个
区间，判断target 这个区间里面，如果不在，则去另一个区间查找

  4567 012
  本写法用的是左闭右闭(二分查找)
1.我们用 nums[left] <= nums[mid]，来判断mid是落在左边的递增数组
  *为什么用 =，因为当[left] = [mid]时，mid也是在左边的递增数组
  
  *当 nums[left] <= target < nums[mid]：说明target在[left,mid)
  所以right = mid-1, [left,right] = [left,mid)
  
  else: #target >= num[mid]
   为什么可以 left = mid + 1,假如说target = [mid]的时候，不就错过了？
   *不会的，因为假如说[mid] == target,早在第一个if 判断就已经剔除出去了
   *所以这里等于是 target = [mid,right],但是target不可能等于mid,所以left = mid + 1
   *[left,right] = [mid+1,right]        

2.假如说target没在大递增数组那就在小递增数组
    
  if nums[mid] < target <= nums[right]:
  在target在小递增区间内
  [mid] != target我们是知道的（如等于在之前就被剔除）,因为是左闭右闭写法，所以<= right
  left = mid + 1无悬念，因为取不到target不可能等于mid
  
  else: target在递增区间内，
  right = mid - 1,因为 target不为mid
  
注意，这题同时是可以处理，4567 002这种情况（中间有重复的数字，而非两边）
"""




