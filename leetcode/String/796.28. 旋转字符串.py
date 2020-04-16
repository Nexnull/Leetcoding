"""
这个题目说的是，给你两个字符串 A 和 B
你要判断字符串 A 是否可以通过将左边的若干字符旋转到右边
来得到字符串 B。如果可以就返回 true，否则返回 false。
比如说，给你的两个字符串是：
A = "abcde"
B = "cdeab"

"""

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        if len(A) != len(B):
            return False

        aa = A + A
        laa = len(aa)
        lb = len(B)

        # 这里+1 的目的是，假如说是空字符串，那么则进不了这个循环
        # 但我们在下面 pb < lb, 进行了处理，使得不会index outof range
        for start in range(len(A) + 1):
            pa = start
            pb = 0


            while pa < laa and pb < lb and aa[pa] == B[pb]:
                pa += 1
                pb += 1

            # 假如说a 旋转后可以得到 b的话
            # 那么pb 最后肯定会+1使得长度 == lb
            if pb == lb:
                return True

        return False

"""
// Time: O(n^2), Space: O(1)
https://algocasts.io/episodes/Y9pJaeGA
A = "abcde"
B = "cdeab"

我们要判断abcde 旋转后可不可以得到 cdeab
最好的做法是， 把A拼接起来, 变成 abcdeabcde， 然后每一次都与 cdeab进行双指针对比
如果b的指针可以遍历到最后，那么说明这两个字符串可以拼接到一起

"""