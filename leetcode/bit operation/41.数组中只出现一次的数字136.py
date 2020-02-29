class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array and len(array) == 0: return None

        xor = 0 ; mark = 1
        for num in array: xor ^= num
        # 找到xor最右边的第一个分叉1，用此来确定分组
        while xor & mark == 0: mark <<= 1

        x = 0 ; y = 0
        for num in array:
            # print(num&mark)
            if num & mark == 0:
                x ^= num
            else:
                y ^= num
        return [x,y]


if __name__ == "__main__":
    solution = Solution()
    solution.FindNumsAppearOnce([1,2,2,3,3,4])


"""
Time: O(n), Space: O(1)
已知 x^x = 0(相同的两个数字 ^ 为0,所以这里，我们假如 2,2,1,1,3 一直异或，最后会剩下一个3
以上方法可以用来找数组中只有一个数字是只出现一次
但对于这题，我们需要把两个不同的数分成两个组来，然后异或求出只出现一次的数

答案
1.xor,这是用来记录数组中两个只出现一次数的 异或值 1000 ^ 0010 = 1010
2.我们用mark = 1,来查找xor的从右往左的第一个分叉，例如在这里找到的是 10（1）0，找到这个1，说明在这个位置上
单数a,b 必有一个这个位置上是1。
3.我们根据在mark这个bit上是不是1，来进行分组，分成两组，a,b两个数必分开存在这两组
4。然后用x,y = 0,0.分别来异或这两个组，最后返回[x,y]

"""
