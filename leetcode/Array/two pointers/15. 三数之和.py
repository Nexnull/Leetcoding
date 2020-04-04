"""
Given an array nums of n integers, are there elements a, b, c
in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return

        res = []
        nums.sort()
        for index in range(len(nums)-2):
            #查看当前的nums[index]和上一个index是否相同，如相同则跳过，因为会产生相同的结果
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left , right= index + 1 ,len(nums)-1
            while left < right:
                s = nums[index] + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    res.append([nums[index],nums[left],nums[right]])

                    #假如说当前循环left,right左右都有相同元素，则进行一次去重处理，不然会返回相同结果
                    # 例如 1,2,3,3,3,4 那么这个left最终会停留到最后一个3， 因为[3,4]是不相同的
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # 同理这个 1,2,3,3,3,4 这个right最终会停留到最左的一个3，因为[2,3]不同
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    #res已经append了当前这个重复数字，当前我们的l,r还停留在最后一个重复数字上
                    #所以我们最后要移动一下
                    #直到执行完下一步操作left,right才摆脱重复数字
                    left += 1
                    right -= 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-3,-2,0,1,2,5]))


"""
答案：
1.暴力解，都是枚举，O(n^3)
2.枚举a,b, 则c 我们知道是-(a+b),然后我们把nums放在一个set里，每次查c都是从set里面查
  枚举a,b .查c, 时间复杂度O(n^2)*O(1) ,空间复杂度O(n),因为开了一个set
  
3.sort and find(two pointer) 
  1。首先先把数组sort一遍，O(nlogn)
  2。开始遍历数组，定遍历的指针为index,[index,-1,0,1,2,3]
  3。然后创建两个指针，left是index右的第一个元素，right是列表最后一个元素
  3。开始一个while 循环，当 index + left + rigth > 0时，right左移，反之left右移
  4。找到返回true,没找到推出循环返回false
  两个循环 O（n^2)

注意：
    假如说单纯按照方法3来写的话，有可能会出现重复的数导致出错，例如【0,0,0,0,0],那么直接把
    所有符合要求的答案都加进res的话，就会输出[[0,0,0],[0,0,0],[0,0,0]]
    所以我们还要进一步对代码进行处理
"""