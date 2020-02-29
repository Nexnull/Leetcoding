class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if (numbers == None or len(numbers) == 0):
            return False

        for i in range(len(numbers)):
            while numbers[i] != i:
                #前提是，number[4] = 3 并不等于 4
                #但是在这里， number[4] = 3 却等于 number[3] = 3
                #这就意味着 【0，0，0，3，3，x, x]
                # index4存在一个3，却发现3这个位置已经有人占定了，说明重复
                if (numbers[i] == numbers[numbers[i]]):
                    duplication[0] = numbers[i]
                    print(duplication)
                    return True

                temp = numbers[i]
                numbers[i] = numbers[numbers[i]]
                numbers[numbers[i]] = temp

        return False




if __name__ == "__main__":
    solution = Solution()
    solution.duplicate([2,3,1,0,2,5,3],[0])



"""
这题本来就不算是难题吧，关键是要给出一个比较好的解法：
1。可以利用排序来做，然后看下一位是否相同，来判断
2。可以利用字典来做

链接：https://www.nowcoder.com/questionTerminal/623a5ac0ea5b4e5f95552655361ae0a8?answerType=1&f=discussion
3。数组的长度为 n 且所有数字都在 0 到 n-1 的范围内
我们可以将每次遇到的数进行"归位"，当某个数发现自己的"位置"被相同的数占了，则出现重复。

举个栗子：
以数组 {2,3,1,0,2,5,3} 为例
当 i = 0 时，nums[i] = 2 != i，判断 nums[i] 不等于 nums[nums[i]]，交换 nums[i] 和 nums[nums[i]]，交换后数组为：{1,3,2,0,2,5,3}
此时 i = 0，nums[i] = 1 != i，判断 nums[i] 不等于 nums[nums[i]]，交换 nums[i] 和 nums[nums[i]]，交换后数组为：{3,1,2,0,2,5,3}
此时 i = 0，nums[i] = 3 != i，判断 nums[i] 不等于 nums[nums[i]]，交换 nums[i] 和 nums[nums[i]]，交换后数组为：{0,1,2,3,2,5,3}
此时 i = 0，nums[i] = 0 = i，继续下一组
当 i = 1，nums[i] = 1 = i，继续下一组
当 i = 2，nums[i] = 2 = i，继续下一组
当 i = 3，nums[i] = 3 = i，继续下一组
当 i = 4，nums[i] = 2 != i，判断 nums[i] 等于 nums[nums[i]]，出现重复，赋值返回
"""