class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0

        candy = [1 for i in range(len(ratings))]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candy[j] = max(candy[j], candy[j + 1] + 1)

        return sum(candy)

"""
 // Time: O(n), Space: O(n)
https://algocasts.io/episodes/dbGYvyp5
由于题目要求的是，评分高的孩子要比评分低的孩子分配的糖果数量要多
所以我们就能默认 评分低的孩子（低于两边），只能分到一颗糖果
那么评分高的孩子，怎么看，就是比左边分高，或者比右边分高，或者比左右两边分都高的，就理应拿更多糖果

做法是从左往右扫一遍，再从右向左扫一遍，扫到比自己小的，自己就取一个更大一点的
"""