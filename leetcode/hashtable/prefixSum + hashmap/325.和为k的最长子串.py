"""
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

链接：https://www.jianshu.com/p/7108226dc023

"""
import collections
class Solution(object):
    def findMaxLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        prefixSum = collections.defaultdict(int)
        prefixSum[0] = -1
        Sum = 0
        maxSubLen = 0

        for i in range(len(nums)):
            Sum += nums[i]
            if (Sum - k) in prefixSum.keys():
                maxSubLen = maxSubLen(maxSubLen, i - prefixSum[Sum - k])

            if Sum not in prefixSum.keys():
                prefixSum[Sum] = i

        return maxSubLen

"""
答案：
这次的写法和560就不一样了，因为这里我们用的hashmap储存的 key,value是不一样的
因为这里是要求子串的最大长度，  所以这里的key我们放的依旧是sum, 但是value放的是index

1. 同样的，我们持续维持着一个sum , 当sum - k 在prefixsum.keys()里的时候， 说明存在一个连续的子串，和为k
   这时，我们用当前的 index - 那个连续子串的前一位index, 得到的就是当前子串的长度
   
   k = 10 sum = 25
   [8 7 |1 2 3 4]
   
   prefixSum[25-10] = prefixSum[15] = 1
   i = 5
   5 - 1 = 4
   
2. k = 10 sum = 10
   [1,2,3,4]
   prefixSum[10-10] = prefixSum[0] = ?
   i = 3
   所以应该返回4，所以在这题，prefixSum[0] = 要等于 -1

3.为什么这里要当 Sum不在prefixSum里的时候才 更新
  因为这里是要求最长，而不是最短，要保持最长的话，我们就要记录最开始的index,这样用当前的index 去减之前的index才够
  够大

"""