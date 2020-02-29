"""
Given a 32-bit signed integer, reverse digits of an integer.
Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]
Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321
"""
def reverse1(self, x):
    if not x: return x
    sign = x//abs(x)
    x *= sign
    res = 0
    while x != 0:
        res = x%10 + res*10
        x //= 10

    if res >= (1 << 31)-1:
        return 0
    return res*sign

"""
1.首先我们要返回一个数的相反数，我们得确定这个数是（正，负）-sign
2.之后我们让 x变为正数，为了不让其影响while循环的执行
3.while x != 0, 因为我们处理x的一位数，就要让它 x//=10,所以当x == 0时代表x已经被处理好了
4. res = x%10 + res*10, 把res放大，腾出个位给x%10
5. 处理异常情况， res的取值范围应该在 [−2^31,  2^31 − 1]之间
6. 返回res 时带上它应有的符号
"""