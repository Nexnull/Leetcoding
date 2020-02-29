import random
class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    #Time: O(n), Space: O(1)
    def shuffle(self):
        ans = self.nums[:]                     # copy list
        for i in range(len(ans)-1, 0, -1):     # start from end
            j = random.randrange(0, i+1)    # generate random index, [0,i]里随便取一个数
            ans[i], ans[j] = ans[j], ans[i]    # swap
        return ans


"""
https://algocasts.io/episodes/VXGOkqGQ
其实这个题是为了讲一个随机算法,Fisher–Yates shuffle 算法
Fisher–Yates shuffle是对有限序列生成一个随机排列的算法，所有的排列是***等概率***的
例如有n张牌，那么按照这个算法，总共能洗出 N!种结果，每种结果出现概率都是 1/n!

这个算法的实现：https://www.youtube.com/watch?v=tLxBwSL3lPQ
"""