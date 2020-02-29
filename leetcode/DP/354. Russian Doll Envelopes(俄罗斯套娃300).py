"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both the width and height of one envelope is
greater（严格大于哦） than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)
Note:
Rotation is not allowed.
Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""
#DP，比较慢
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes or len(envelopes) == 0:return 0

        res,length = 0, len(envelopes)
        envelopes.sort(key = lambda x:x[0])
        dp = [1]*length

        for i in range(length):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[j] + 1, dp[i])
            res = max(res,dp[i])
        return res


"""
time: O(n^2) space;O(n)
这题其实就是300.寻找最大子串dp做法的变种，只不过找最大字串那题的数组是一维的，且排序好的。
这里的数组是二位的且没排序，所以我们要先把它排序好，然后在用300的方法去做
"""

# 二分查找，快
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0

        reslen, n = 0, len(envelopes)
        envelopes.sort(key=lambda a: (a[0], -a[1]))
        res = [0] * n

        for e in envelopes:
            index = self.searchInsert(res, reslen, e[1])
            res[index] = e[1]
            if reslen == index:
                reslen += 1
        return reslen

    def searchInsert(self, array, length, target):
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

"""
https://blog.csdn.net/qq_17550379/article/details/88060945
这个人的思路和algocast的思路是一样的，关于binarysearch的做法，可以先回顾下300题
答案：
1.首先得把envelopes给排序了，优先级按照e[0],-e[1]排，因为我们先保障e[0]是递增的
然后后面我们就不需要考虑e[0]了
2.现在来说说为什么要按照-e[1]排（从大到小）
  假如说遇到了[[1,1],[1,2]],我们使用后面大的能往加进res的做法的话
  这种情况是合法的，但事实上是不合法的，因为e[0]要严格大于
  
  所以我们sort后变为[[1,2],[1,1]],先把[1,2]加进res了，那么遍历到[1,1]的时候就不会把它给加进去了
  
3.其实也没啥了，后面的就是for循环，来对比e[1]的大小来使 reslen++


注意：我们可以利用buildin bisect_left() 来代替我们自己写的一个二分查找的函数
300.https://blog.csdn.net/qq_17550379/article/details/82871892
354.https://blog.csdn.net/qq_17550379/article/details/88060945
"""