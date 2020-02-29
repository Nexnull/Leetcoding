class Solution:
    def reOrderArray(self, array):

        odd = []
        even = []
        for i in range(len(array)):
            if array[i] % 2 == 1:
                odd.append(array[i])
            else:
                even.append(array[i])

        odd.extend(even)
        print(odd)
        return odd




if __name__ == "__main__":
    solution = Solution()
    solution.reOrderArray([4,1,3,2,7])

"""

1。一开始看到这题的感觉，就第一时间想到快速排序，把所有比标志元素大的往前排，把所有比标志
元素小的往后排。
打算用两个指针从头往后遍历，一个遍历奇数，一个遍历偶数
遍历奇数的指针要快点，遍历偶数的指针要慢点，交换


2。发现这样做行不通，后面打算用插入排序的做法，每次找到奇数，往前插，这样就只需要一个指针,但是一个问题，这样插的话指针可能会混乱。（因为一个数组在不断变长）

3。又想到一个方法，空间复杂度高一点，用两个数组，奇数一个数组，偶数一个数组，找一就放一个，最后拼接起来
返回，这种写法最快最方便
"""



