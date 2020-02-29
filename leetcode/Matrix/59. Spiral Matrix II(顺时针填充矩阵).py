"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[[ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]]
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(n)] for j in range(n)]
        left = 0
        right = n-1
        top = 0
        bottom = n-1
        num = 1

        while True:

            for i in range(left,right+1):
                res[top][i] = num
                num += 1
            top += 1
            if top > bottom:
                break

            for i in range(top,bottom+1):
                res[i][right] = num
                num += 1
            right -= 1
            if right < left:
                break

            for i in range(right,left-1,-1):
                res[bottom][i] = num
                num += 1
            bottom -= 1
            if bottom < top:
                break

            for i in range(bottom,top-1,-1):
                res[i][left] = num
                num += 1
            left += 1
            if left > right:
                break

        return res

"""
https://leetcode.com/problems/spiral-matrix-ii/discuss/22289/My-Super-Simple-Solution.-Can-be-used-for-both-Spiral-Matrix-I-and-II
这题其实也是顺时针打印（顺时针遍历）
但是为什么这里是while 是left <= right, top <= buttom呢？
而在顺时针打印那题是left < right，违背了就退出了。回去研究下

其实关键不在于大于小于号，而是在于left <= right这种写法，只适用于n*n的矩阵，一旦出现n*m的矩阵
那么就容易出现指针乱动的情况， 所以为了应对这种情况，我们选择鲁棒性更高的写法，每执行完一次for循环
我们都判断一下，如果没问题，就接着走，如果有问题，我们就直接退出循环了
"""

