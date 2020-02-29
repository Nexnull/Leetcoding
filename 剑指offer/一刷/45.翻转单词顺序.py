""""
单考虑完成的话就是[::-1]了
special 是用来应对"" "  " 这种情况的

"""
class Solution:
    def ReverseSentence(self, s):
        special = s
        s = s.split()
        if s == []:
            return special
        return " ".join(s[::-1])



if __name__ == "__main__":
    solution = Solution()
    solution.ReverseSentence(" ")