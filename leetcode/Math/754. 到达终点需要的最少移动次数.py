class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        res = 0
        sum = 0

        while sum < target or ((sum - target) & 1) == 1:
            res += 1
            sum += res

        return res


"""
https://algocasts.io/episodes/yRp3edm4
Time: O(n), Space: O(1)
这题比较tricky

这题相当于是 1 2 3 4 5 6... 中间一直加符号，直到最后到达target, 然后问最少能用几个数

我们可以总结出以下几个规律
假设我们先无脑一直加
假如说 sum < target, 那么就意味着我们可以一直加这些数
假如说 sum == target, 我们可以直接返回res
假如说 sum > target, 那么说明，这个序列并不能一直加，肯定有数是减号的
    那么假设 sum - target = x, 说明超出了x个数, 那么我们要怎么修正它使得能让 sum == target呢？
    移动一下 sum - x = traget
    我们也直到改变一个数字 n 的符号 （从+变-），等于减少2n
    所以实际上 sum - 2n = target
    再变一下 sum - target = 2n， 是个偶数
    所以说， (sum - target) & 1) == 1， 那么sum还没超出target,则要继续加
    如果超出了， 我们也可以默认存在某个数，可以使得改变符号来让 sum == target
    
"""