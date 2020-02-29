"""
这个题目说的是，从 0 到 n 这 n+1 个整数中去掉一个，然后把剩下的 n 个整数放进一个长度为 n 的数组，给你这个数组，你要找到那个去掉的整数。

比如说，给你的数组是：

4, 1, 0, 2

这里的数组长度是 4，说明这是从 0 到 4 中去掉一个数字后形成的数组。数组中缺失的数字是 3，因此我们要返回 3。
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ nums[i] ^ i
        return res

"""
// Time: O(n), Space: O(1)
https://algocasts.io/episodes/vkmebGbP
答案：
1.还是x^x = 0 ， x^0 = x的操作
2.这里写法要有点讲究，使得可以用一次循环去把所有答案给求出来

此题可以和41题对照来看
"""