"""
这一题有说，上一行的所有值比下一行的所有值小
"""
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array or len(array) == 0:
            return False

        row = len(array)
        col = len(array[0])
        top = row -1
        right = 0

        while top > -1 and right < col:
            if target > array[top][right]:
                right += 1
            elif target < array[top][right]:
                top -= 1
            else:
                return True
        return False



if __name__ == "__main__":
    solution = Solution()
    print(solution.Find(7, [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]] ))



"""
我的做法是，分别做两次二分查找，先竖再横，但是测试条件定的比较宽泛，例如第二行的最后一个比第三行的第一个要大
[[1,2,8,9],
 [2,4,9,12],
 [4,7,10,13],
 [6,8,11,15]]


答案：
* 矩阵是有序的，从左下角来看，向上数字递减，向右数字递增，
* 因此从左下角开始查找，当要查找数字比左下角数字大时。右移
* 要查找数字比左下角数字小时，上移
注意while循环的区间设定，top > -1,因为top可以为0

二刷：
为什么我们一定要挑左下角来开始呢？
因为左下角：(x,y)上面都是比(x,y)小的数字，(x,y)右边都是比(x,y)大的数，所以我们可以利用这个规律去找
但是：
左上角，右边和下面都是比(x,y)大的数字，无法根据与target的关系进行查找
右下角，左边和上面都是比(x,y)小的数字，无法根据与target的关系进行查找
所以我们知道了，这题的解题关键是，要能根据(x,y)与target的关系来进行移动，才能找到target

我们这样看
1.小表示比当前数字小，大表示比当前数字大，未知表示未知
2.因为我们是从最后一行上来的，所以表示对于最下面的一行来说，都比target 大，也就是都无效了
3.因为我们是从左向右走的，说明，左边，以及左边的上面，都比target小，都是无效的
4.所以我们要去探索未知的值
小 小 小    未知           废  废  废  x
小 小 小    未知 =====》   废  废  废  x
小 小 (x,y) 大            废  废 check x
大 大 大    大            废  废  废  废

根据这个原理，我们也可以从右上角往左下角进行查找。
"""
class Solution(object):
    def searchMatrix(self, array, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not array or len(array) == 0:
            return False

        row = len(array)
        col = len(array[0])
        top = 0
        right = col-1

        while top < row and right > -1:
            if target > array[top][right]:
                top += 1
            elif target < array[top][right]:
                right -= 1
            else:
                return True

        return False