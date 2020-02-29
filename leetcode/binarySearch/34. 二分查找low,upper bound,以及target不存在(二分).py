class Solution(object):
    def findleft(self, nums, target):
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

            if nums[mid] == target:
                index = mid
        return index

    def findright(self, nums, target):
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

            if nums[mid] == target:
                index = mid
        return index

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.findleft(nums, target)
        right = self.findright(nums, target)
        return [left, right]

"""
二分查找有几种写法？它们的区别是什么？ - labuladong的回答 - 知乎
https://www.zhihu.com/question/36132386/answer/712269942

二分查找的upper bound和lower bound

核心点1：
这里为什么 target == nums[mid]的时候，不返回答案：
因为我们要不断的挪动mid的指针，直到挪不动的时刻（while被破坏了）,这时候mid才指向upper bound或者lower bound


核心点2:
target (<,<=) nums[mid]
<时，right左移，而等于时，left却右移，使得mid偏向右边界
<=时，right左移，等于时，right还是左移，使得mid偏向左边界
例子：nums={ 1,2,3,3,3,3,4,5 } target=3
假如说：target <= nums[mid] 最后出来的结果：1,2(right),3(left,mid),3,3,3,4,5  
假如说：target <  nums[mid] 最后出来de结果：1,2,3,3,3,3(right),4(left,mid),5

核心点3：
那么假如target不存在呢？比如 nums={1,2,4,5} target=3
当判断条件为if (target <= nums[mid])，最终位置状态为 1,2(right),4(left,mid),5
当判断条件为if (target < nums[mid])，最终位置状态为  1,2(right),4(left,mid),5

我们可以利用target不存在的这个规律，来作出一种解答：退出循环时，left在空target的右边一位
                                                         right在空target的左边一位
                                                         利用这个规律，我们就可以去解决35这种题

                                   

但是这种二分查找有缺陷的地方，<=,就是当[2,2] 3这种case 出来以后， 2,2(right),left(out of range)
所以这里采用了一种聪明的做法，就是利用index,来记录mid
  每个函数我们都初始化一个index = -1
  1.
  假如说在过程中我们找到了[mid] == target
  if nums[mid] == target: index = mid 
  那么index = mid, 所以最后可以直接retrun index
   
  2。假如说我们没找到[mid] == target
  所以index 还是等于-1,直接return index



"""