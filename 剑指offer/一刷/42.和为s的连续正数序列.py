
class Solution:
    def FindContinuousSequence(self, t):
        res = []
        left = 0
        right = 1

        while right < t:
            list = [i for i in range(left,right+1)]
            total = (left + right)*(right-left+1)//2
            if total > t:
                left += 1
            elif total < t:
                right += 1
            else:
                res.append(list)
                right += 1

        print(res)




if __name__ == "__main__":
    solution = Solution()
    solution.FindContinuousSequence(1)


"""
这题是43题和为s的两个数的升级版本，我感觉是要用递归来做的
但是没有什么想法
答案说用双指针，想了一想，似乎有道理
可以把指针放成第一个和第二个，太小，则right+=1，太大则left+=1
做出来了。。

然后做法可以聪明点，求和可以用（首+末）*项数/2 , 用sum（）的话就提升了时间复杂度
"""