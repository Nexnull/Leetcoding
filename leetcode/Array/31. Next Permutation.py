"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
改变数组的元素位置，找出比当前数字大的下一位数字，如果没有返回reverse
"""
class Solution(object):
    def swap(self,nums,i,j):
        nums[i],nums[j] = nums[j],nums[i]

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums is None or nums < 2: return nums

        # step1从低位向高位遍历，找到第一个非递增的数（1）
        p = len(nums) - 2
        while p >= 0 and nums[p] >= nums[p+1]:
            p -= 1


        #step2,然后再从低位向高位遍历，找出一个比（1）的大的数字(2)
        #假如说是321这种，p已经是等于-1了。我们就可以直接跳过这个if语句
        if p >= 0:
            i = len(nums) - 1
            while i > p and nums[i] <= nums[p]:
                i -= 1
            self.swap(nums,i,p)

        #step3，把p后面的元素进行，交换后重排序（反转）
        #同时，假如说是321，这种递增的，已经达到最大值了，它的next permutation就是反过来123
        i = p + 1
        j = len(nums) -1
        while i < j:
            self.swap(nums,i,j)
            i , j = i+1, j-1


"""
https://algocasts.io/episodes/QrWZJbW5
Time: O(n), Space: O(1)
ex:218421
答案：
因为我们要找比当前大的下一个排列，就意味着我们不能从高位找，只能从低位开始找（改变较小）
因为对于低位的递增的8421，这四个无论怎么排，我们都找不到比他更大的排列（已经是最大排列）
1.从低位向高位遍历，找到第一个非递增的数（1）
2.然后再从低位向高位遍历，找出一个比（1）的大的数字(2)，交换这两个数字(1),(2)
2, 1, 8, 4, 2, 1 交换1，2，得到2，2，8，4，1，1
（因为8421是递减的，所以我们得从1->8,这样才能确保找到改变最小的数）

2，2，8，4，1，1
交换后我们发现，并不是最小的更大值，所以我们要把8411重排序，来让它变成一个最小值

因为正常来说，交换后得到的数是从大到小排列的，所以我们只要把它反过来，就能得到从小到大排列
3.利用双指针互换的方法，把8411反过来，（因为8411是递增的，所以反过来是最小的）

注意：
1.while p >= 0 and nums[p] >= nums[p+1]: p -= 1
这里p>=0，因为当我们发现这个数组一直递增的时候，我们要让p = -1
还有当我们遇到相同数字是，p依旧要继续移动

"""
