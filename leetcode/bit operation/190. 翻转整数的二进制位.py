class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if not n:
            return 0

        res = 0
        for _ in range(32):
            res = (n & 1) | (res << 1)
            n >>= 1

        return res

"""
// Time: O(1), Space: O(1)
https://www.youtube.com/watch?v=K0EHvvbUdEg
这个的原理和翻转整数是有点像的：
10进制
res = res*10 + n%10
n /= 10

二进制：
res = res*2 + n%2
n /= 2
其实上面这个操作和下面的是一样的
res = res>>2 | n&1
n >>= 1
"""