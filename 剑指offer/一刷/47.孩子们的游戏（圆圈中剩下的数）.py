class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1

        last = 0
        for i in range(2,n+1):
            last = (last + m) % i
        return last


if __name__ == "__main__":
    solution = Solution()
    solution.LastRemaining_Solution(11,3)


"""
又是一道看了让人不明所以的题
可惜还是没啥想法
https://blog.csdn.net/u011500062/article/details/72855826

答案：
还是不太懂，以后再说吧
1.方法1，把一个列表作为环状链表，然后每一次把第m个数给清理出去，i为被清理那个数的下标

2.这是一个叫约瑟夫环的问题，它的递推式为（N为人数，M为第几个人出列）
last = f(n-1,n)

记住这个递推式子就好了
0                        n = 1
f(n,m)=(f(n−1,m)+m)%n    n > 1

"""