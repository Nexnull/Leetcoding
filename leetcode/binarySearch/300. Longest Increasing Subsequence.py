"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
资料：https://algocasts.io/episodes/yRp3Mym4
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        length = len(nums)
        res = [0]*length
        res[0] = 1

        for i in range(1,length):
            for j in range(i):
                if nums[i] > nums[j]:
                    cur = res[j] + 1
                else:
                    cur = 1
                res[i] = max(res[i],cur)

        len_max = max(res)
        return len_max

"""
时间复杂度O(N^2) 空间复杂O（N），新开了一个list,比较垃圾
答案：
[10,9,2,5,3,7,101,18]
      j i 
1.准备好递归的列表，且res[0] = 1，因为假如说出现[1]这种列表，那么它的两个for循环是判断不了的,后面讲为什么
2.准备两个for 循环，第一个循环是从1开始遍历到结尾，它是一个确定当前index的最长串是多少的index
3.j是一个index 从0到(i-1)的index, 它的目的就是，扫描i前面的所有数，看看i是否能拼接上前面的列表
4.当nums[i] > nums[j]时，满足题目的递增sequence的要求，所以我们把cur = res[j]+1,若不能，则cur = 1
5,我们要选出一个最长的可能，把它加进res[i]里
6.回到1，因为j总是在i后扫描，当列表元素只为1的时候，它做不到扫描，得不出判断，所以我们得在一开始预设值
"""

class Solution(object):
    """
    这个search Insert为35题的答案,但是这里需要改造一下
    因为我们分配的给res的内存是大于实际需要的内存
    但我们需要的只是前面那一小段有数字的，例[1,2,4,0,0,0]
    只需要到[1,2,4],所以变量length的作用就在这里
    """
    def searchInsert(self, array,length, target):
        left = 0
        right = length - 1

        while left <= right:
            mid = (left + right) // 2

            if array[mid] == target:
                return mid
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def lengthOfLISBinarySearch(self, res,nums):
        if nums is None:
            return []

        n = len(nums)
        res = [0]*n
        reslen = 0

        for x in nums:
            i = self.searchInsert(res,reslen, x)
            res[i] = x
            if i == reslen:
                reslen += 1
        return reslen

"""
时间复杂度O(NlongN) 空间复杂O（N），新开了一个list,二分查找是logN，比较强
答案：
这里的设计其实很巧妙，每次从nums取一个数出来，看它能在res
里放在什么位置，但都是按照从小往大的顺序（满足要求）

case 1,8,4,9...

例如：原来是[1,8],现在遍历到4
1.新遍历到的数字（4），可以插入的位置为res的最右边[1,x]，且[1,8],[1,4]长度相等，那么我们就把[1,8]替换成[1,4]
(最好的策略，为了找除最长字串）
2.新遍历到的数字（9）,可以插入的位置为len(res),[1,4]x,所以能增加res的长度，于是我们把9加进[1,4]->[1,4,9]

"""




