"""
比如说，给你的数字是 5，你要返回帕斯卡三角形的前 5 行。

     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if not numRows or numRows == 0:
            return []

        res = []


        for i in range(numRows):
            # i是每一层的个数，因为i是从0 ~ numrow-1, 所以在下面要进行设置
            temp = [1 for _ in range(i + 1)]

            # j是操作的当前元素
            # j 应该从 [1, jjjj, 1] 第一个数字，和最后一个数字中间操作
            for j in range(1, len(temp) - 1):
                temp[j] = res[i - 1][j - 1] + res[i - 1][j]

            res.append(temp)

        return res

"""
https://algocasts.io/episodes/jwmBr5m8
Time: O(n^2), Space: O(1)
这题主要是边边角角的地方比较多
"""