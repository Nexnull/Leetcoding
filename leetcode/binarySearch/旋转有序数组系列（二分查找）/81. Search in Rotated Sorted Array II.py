"""
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search.
If found in the array return true,
otherwise return false.

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
这个是带重复数字的二分搜索
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums or len(nums) == 0:return False
        while len(nums) - 1 and nums[0] == nums[-1]:
            nums.pop(-1)

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return True

            if nums[left] == nums[mid]:
                left += 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else: #target >= num[mid]
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

"""
best O(logn) worstO(n) space:O(1)
https://www.youtube.com/watch?v=e-UALGfQpOk
答案：
1.这题与33题相比，有可能出现的情况是 [1,3,1,1,1] 3  mid = 1，解决不了
正常情况是左大右小 ，我们通过看mid 是在较大递增区间 还是在较小递增区间来查找target
但这个case, [left] = 1, [mid] = 1,我们就以为mid在大递增区间，事实上mid在小递增区间，于是就会
使得函数在错误的区间上查找target,导致找不到的情况发生

2.所以我们需要把这个特殊情况给去除掉，就是当[left] == [mid],left++,
使得[left] != [mid]就好。
这一步等于是把这个数组多余的，没必要存在的元素给抹除
（因为例如上面的那个case,哪里都有1，删掉干扰项的1其实对整体结果无影响（还是一个大递增区间一个小递增区间））
（有更极端的做法是，假如[0]==[-1],就一直删,删到不等为止）

3.注意2这个步骤应该在所有指针移动之前执行完这个判断，所以它作为if 放在那里

注意，这种题去重的关键在于，第一个if 语句，是用哪两个指针进行判断的，如果那两个指针一开始出现
相同情况的话，就会出现分区错误，导致指针去错地方。81和154都一样
"""