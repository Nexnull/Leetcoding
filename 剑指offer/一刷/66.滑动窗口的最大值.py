
class Solution:
    def maxInWindows(self, num, size):
        if len(num) < size or not size :
            return None

        res = []
        left = 0
        right = size

        for left in range(len(num)-size+1):
            res.append(max(num[left:right]))
            right += 1

        return max(res)

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxInWindows([2],3))


"""
傻逼编译器
这题很简单，难的是需要调整窗口大小的
"""