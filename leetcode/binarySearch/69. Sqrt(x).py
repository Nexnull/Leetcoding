class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        left = 0 ; right = x ; res = 0
        while left <= right:
            mid = (left+ right)//2
            if mid == x // mid:
                return True
            elif mid > x // mid:
                right = mid - 1
            else:
                left = mid + 1
                res = mid

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(6))



"""
https://www.youtube.com/watch?v=CuF7FQtu12o&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=36
此题与leetcode367基本一样
答案：
二分法：
1。界限：left = 0, right = n(这里right直接用n是因为这里不是数组，所以不用担
心out of range), mid= (left + right)//2
2。mid == x // mid 等于 mid*mid == x ,因为有些test case用2^64,所以担心会越界产生错误结果
3。res = mid 放在left那里很有深意，说明res总是处于等于下界的整数，当sqt8时
返回的res = 2。且因为我们是用很安全的二分查找，所以我们不用担心res>right之类的

比较数学的方法：牛顿迭代法
太高级，不谈

"""