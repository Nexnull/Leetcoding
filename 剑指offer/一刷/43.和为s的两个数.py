class Solution:
    def FindNumbersWithSum(self, array, t):
        if array == None:
            return
        left = 0
        right = len(array) - 1
        res = []

        while left < right:
            sum = array[left] + array[right]
            if sum > t:
                right -= 1
            elif sum < t:
                left += 1
            else:
                res.append([array[left],array[right]])
                left += 1

        print(res)
if __name__ == "__main__":
    solution = Solution()
    solution.FindNumbersWithSum([1,2,2,3,3,3,5],6)









"""

答案：
假设：若b>a,且存在，
a + b = s;
(a - m ) + (b + m) = s
则：(a - m )(b + m)=ab - (b-a)m - m*m < ab；说明外层的乘积更小

也就是说依然是左右夹逼法！！！只需要2个指针
1.left开头，right指向结尾
2.如果和小于sum，说明太小了，left右移寻找更大的数
3.如果和大于sum，说明太大了，right左移寻找更小的数
4.和相等，把left和right的数返回
"""