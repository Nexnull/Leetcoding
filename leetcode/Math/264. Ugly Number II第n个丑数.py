"""
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
"""
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:return -1
        res = [0]*n
        res[0] = 1

        p2 = 0; p3 = 0; p5 = 0
        for i in range(1,n):
            minuglynum = min(res[p2]*2,res[p3]*3,res[p5]*5)
            res[i] = minuglynum
            if minuglynum == res[p2] * 2: p2 += 1
            if minuglynum == res[p3] * 3: p3 += 1
            if minuglynum == res[p5] * 5: p5 += 1

        return res[n-1]

"""
Time: O(n), Space: O(n)
答案：
这题是使用dp来做的
1.由于我们想让res里的元素，是丑数从小到大的排序
2.每个丑数都有 *2，3，5的机会，但是要看res[i]的下一位最小是多少
3.由于p2,p3,p5都是代表着res里的index,等于是这几个index*(2,3,5)在竞赛，看哪个的
更小，就放到下一位。
3.由此可以推出第n个丑数的大小

"""

