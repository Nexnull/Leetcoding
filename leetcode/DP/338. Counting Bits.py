"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
calculate the number of 1's in their binary representation and return them as an array.

Input: 2
Output: [0,1,1]
应该返回0，1，2这三个数含有多少个二进制为1的量
"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]*(num+1)

        for i in range(1,num+1):
            res[i] += res[i&(i-1)] + 1
        return res


"""
https://www.youtube.com/watch?v=C1ZKaUq0H88&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=42

答案：
1.我们可以用一个for 循环遍历,然后在里面再用while i&i-1来一个个消0，但这样的时间复杂度是 O n^2

2.time O(n)
这题利用了动态规划以及 i&i-1的的思想
我们知道
res[i] > res[i&(i-1)], 且res[i&(i-1)]我们已在前面就求得了，+1 就代表着被消去的那个1
且我们观察下面就可以知道，这个递推式是确实有道理的
000
001
010
011
100
111
"""