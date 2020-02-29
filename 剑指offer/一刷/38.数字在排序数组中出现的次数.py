class Solution:
    def GetNumberOfK(self, data, k):
        if k not in data:

            return -1

        left = self.getleftK(data,k)
        right = self.getrightK(data,k)

        return right - left + 1

    def getleftK(self,data,k):
        ###查找重复数字中最左边的那个数字位置

        left = 0
        right = len(data) - 1
        while left<=right:
            middle=(left+right)//2
            # 区别在这
            if data[middle] < k:
                left = middle+1
            else:
                right = middle-1
        return left

    def getrightK(self,data,k):
        ###查找重复数字最右边的那个数字位置

        left = 0
        right = len(data) - 1

        while left <= right:
            middle = (left+right)//2
            #区别在这
            if data[middle] <= k:
                left = middle + 1
            else:
                right = middle - 1
        return right


if __name__ == "__main__":
    solution = Solution()
    solution.GetNumberOfK([1,2,2,3,3,3,5,6,7,8,8,8],8)



"""
感觉这个题应该想让你找到一个最快的算法吧
为什么直觉就是二分查找
可是问题来了，当你用二分查找找到以后，要怎么统计他出现的次数呢？
从对应index来前后查
然后后-前


额，这题我原来的做法也是可以，但是现在用的这个做法比较好一点
刚好能看出来二分查找的不同形式


"""