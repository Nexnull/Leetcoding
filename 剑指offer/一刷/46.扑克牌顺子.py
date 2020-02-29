import collections
class Solution:
    def IsContinuous(self, numbers):
        numbers = sorted(numbers)
        total_gap = 0
        countz = numbers.count(0)
        numbers = list(filter(lambda x:x != 0,numbers))

        #判断是非为[1,1,0,0,0]这种情况
        if list(set(numbers)) != numbers:
            return False

        for i in range(len(numbers)-1):
            total_gap += numbers[i+1] - numbers[i]

        total_gap = total_gap - len(numbers) + 1

        if total_gap > countz:
            return False
        else:
            return True







if __name__ == "__main__":
    solution = Solution()
    solution.IsContinuous([1,0,0,2,0])





"""
number是一个int组成的数组
然后我们要判断这个数组是不是顺子
然后就要判断是不是按顺序递增的（0是否能填充到其中）
我想到可以用一个变量gap来表示，gap为 [5] - [4] ,[4] - [3],我们判断
有多少个0以后，

假如说 [0,0,1,3,4] 
gap = (4-3) + (3-1) = 3
然后,三个非0数应该有只有2的差,所以需要1个0去填，而且只要0的数大于这个差
就可以满足条件了

"""