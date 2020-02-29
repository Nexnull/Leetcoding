"""
Input: "123456579"
Output: [123,456,579]

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
"""


class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        self.res = []
        self.helper(S, 0)
        return self.res

    def helper(self, s, pos):
        if len(s) == pos:
            return len(self.res) > 2

        num = 0
        n = len(s)

        for i in range(pos, n):
            num = num * 10 + (ord(s[i]) - ord("0"))

            # 要求0 <= F[i] <= 2^31 - 1
            if num < 0 or num > (1 << 32 - 1): return False

            if len(self.res) < 2 or \
                    self.res[len(self.res) - 2] + self.res[len(self.res) - 1] == num:
                self.res.append(num)
                # 主循环的终止条件，假如说找到了，满足条件的3个元素,那么就会return True
                if self.helper(s, i + 1):
                    return True
                # 执行到这一步，说明并没有找到
                self.res.pop(-1)

            # 在两种条件下会到这里：
            # 1. res长度大于2了，且不满足斐波那契数列
            # 2. 循环到底了，发现结果不对
            # 在这种情况下，其实是以0为开头尝试了很多种答案了，我们是要放弃以这所有可能
            # 同时，放在这里的目的是，保护 1101 [1,1,0,1]这种情况，因为他是可以成功的
            # 假如说一串数字的首位里面出现了0，说明这一串数字都可以不要了

            # 这里是有trick的，我们这种做法下，即使是 0123，也能返回出正确的【1，2，3】
            # 是因为我们使用了数字加进res, "01" = 0*10 + 1 = 1
            # 但实际上，这隐藏的"01"是不被允许的
            # 因此在回溯中中，我们只要在回溯，发现有一种情况不符合，例如[0,12],到了这里
            # 我们就立刻把"0"开头的这种可能完全去除
            if i == pos and s[i] == "0": return False


"""
https://www.youtube.com/watch?v=X2Udwh28muM
答案：
1.构成斐波那契数列，至少需要三个元素，所以我们res,至少得有三个元素
2.本题是用回溯法的思想来做，原因是我们要一个个地构造子序列来进行拼凑，如果一个子序列不行
  我们就要删除掉,尝试下一个子序列
3.如果数组中有数字为0，那么直接为false(为什么）

"""
