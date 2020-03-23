"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
"""
# 二分查找
# Time: O(n*log(n)), Space: O(1)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums and len(nums) == 0:return 0

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left

"""
1.利用鸽子洞原理，在1-n个位置放n+1个数，必定会有数字是重复的
2.我们就利用这个原则来进行二分查找，选定mid,看有多少个数<= mid
假如说有>mid个数小于mid,说明重复的数字在mid左边
不然重复的数字就在mid右边
3.一直按照这个原则二分查找，循环结束时说明找到了这个数
"""
# 数组的快慢指针法
# Time: O(n), Space: O(1)
class Solution2(object):
    def findDuplicate(self, nums):
        if nums is None or len(nums) == 0: return None

        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
"""
弗洛伊德的乌龟和兔子（循环检测）
算法：
首先，我们可以很容易地证明问题的约束意味着必须存在一个循环。因为 nums 中的每个数字都在 1 和 n 之间
所以它必须指向存在的索引。此外，由于 0 不能作为 nums 中的值出现，nums[0] 不能作为循环的一部分。

因为假如说每个index上都是对应不同的数字，那么就永远不会产生循环，因为每一次去的都是不同的位置
但是假如说有两个index上有相同的数字，那么他们则会进入一个循环当中，因为必定会进到同一个位置（重复数字）

链接：https://leetcode-cn.com/problems/find-the-duplicate-number/solution/xun-zhao-zhong-fu-shu-by-leetcode/
"""