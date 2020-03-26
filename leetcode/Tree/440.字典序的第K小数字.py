class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        cur = 1
        while k > 1:
            gap = self.findgap(cur, cur + 1, n)

            # 说明k要超过了第一第二个前缀的差
            # 那么我们要找第二和第三个前缀
            if gap <= (k - 1):
                k -= gap
                cur += 1
            # 若没超过,说明k在 第一前缀和第二前缀的中间
            # 那么我们就进入下一层寻找 例如 10 11之间还有可能有下一层
            else:
                cur = cur * 10
                # 因为进入下一层只需要移动一次
                k -= 1
        return cur

    # 这个函数是找出当前前缀 和下一个前缀,之间的差距
    # 例如 1 2 之间 ， 1作为所有前缀，拥有多少个元素
    def findgap(self, a, b, n):
        gap = 0

        while a <= n:
            # 假如说 B > N+1 的话， 就像N = 198, B = 200
            # 我们探查到的数已经远远超出了N的范围了，这是不可能的，所以我们最大能探查的n
            # 之所以是n+1, 因为a最多能到n, b要比a至少后一位，所以是b+1
            gap += min(n + 1, b) - a
            a = a * 10
            b = b * 10

        return gap

"""
https://www.youtube.com/watch?v=yMnR63e3KLo视频感觉讲的也不算特别清楚
题解讲的还可以
https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/solution/ben-ti-shi-shang-zui-wan-zheng-ju-ti-de-shou-mo-sh/
"""
