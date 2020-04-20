import collections
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """


        prefixSum = {}
        prefixSum[0] = 1
        Sum = 0
        res = 0

        for i in range(len(nums)):
            Sum += nums[i]
            if (Sum - k) in prefixSum:
                res += prefixSum[Sum - k]

            prefixSum[Sum] = prefixSum.get(Sum, 0) + 1
        return res

"""
思路：https://www.youtube.com/watch?v=0rCaikfA7No
代码：https://blog.csdn.net/fuxuemingzhu/article/details/82767119
答案：
1。prefixSum 就是遍历到i 的时候， sum(nums[:i+1])
我们把每个prefixSum 都作为key, 把这个sum出现的次数作为value

2。为什么要查 Sum - k 在不在prefixSum 的keys里?
因为假如说 Sum - k 在prefixSum 里，就意味着存在一个j,使得 sum( nums[j...i]) 的和是k
那么从 j - i,这个连续序列，就是我们想要找到的和为k的 连续序列

3。为什么prefixSum[Sum] += 1?
因为序列中有可能出现负数，例如 [2,3] 和 [2,3,-1,1], 他们的prefixSum都是相同的，但是最后
的序列是不一样的。

4。为什么要设置prefixSum[0] = 1
因为在正常情况中，sum = 0是达不到（我们无法吧key = 0的情况加进字典），但是我们有可能会有一个字串sum - k = 0
此时res 会要求把 key=0时value的数 取出来。所以我们要把它初始化为1
"""