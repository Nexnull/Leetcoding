"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2} 为 {1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

"""
class Solution:
    def minNumberInRotateArray(self, nums):
        if not nums:
            return
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) //2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == "__main__":
    solution = Solution()
    print(solution.minNumberInRotateArray([3,4,5,6,1,2]))


"""
153. Find Minimum in Rotated Sorted Array
154. Find Minimum in Rotated Sorted Array II
https://algocasts.io/episodes/q2m5w5pz
答案：
1.这题有个特性，是递增数组，像右旋转后，然后问最小值。根绝题意我们可以知道，最小值一定在数组的右半部分
2.所以我们进行二分查找的时候，第一步先看mid是在左半部分还是在右半部分

3.mid 在左半部分，则left = mid + 1,因为mid是在左半部分，所以我们要加一跳过mid
(事实上，当mid到了右半部分，则left的值再也没变化过了）
4.mid 在右半部分，则right = mid,因为最小值在右半部分，我们不能right = mid-1,因为怕mid就是最小值

5.写法采用的是左闭右闭，而我们查找的方法会使得left,right向最小值靠近，所以当len[left,right] =1 
时，区间内唯一的一个值就是最小值

注意：
这里的 while left < right ,意味着当 left>=right时，退出循环，因为我们当找到一个数是
len([left,right]) == 1,时，就意味着找到了那个最小值
"""