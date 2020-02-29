"""
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().
Example 1:
Input: 1
Output: [7]
Example 2:
Input: 2
Output: [8,4]
"""
# The rand7() API is already defined for you.
def rand7():
    pass
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        rand40 = 41
        while rand40 > 40:
            rand40 = (rand7() - 1) * 7 + rand7()
        return rand40 % 10 + 1



"""
https://algocasts.io/episodes/JNmDVZpO
这题存在有数学推理，但是基本道理就是只要x > y,就能用randx 代表 randy
1.我们使用(rand7() - 1) * 7 + rand7()来构造一个大于rand49()
因为最小值是 (1-1)*7 + 1 = 1
    最大值是 (7-1)*7 + 7 = 49
所以(rand7() - 1) * 7 + rand7()是在1-49里随机取
2.我们要求rand40 <= 40时才推出循环，即1-40才退出循环，rand40 % 10 + 1 = [0,9]+1
"""