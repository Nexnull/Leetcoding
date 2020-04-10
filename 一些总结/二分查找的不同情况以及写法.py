"""
@@@@@ 最牛逼的 @@@@@@@@@@@@
二分查找有几种写法？它们的区别是什么？ - labuladong的回答 - 知乎
https://www.zhihu.com/question/36132386/answer/712269942


二分查找有很多限定条件，例如循环中的left < right,这里的不等号要不要加=
还有mid = (left+right) // 2
以及判断完之后，left = mid + 1 这里是一个加一，一个减一，还是都不加不减，还是都加都减

[1,2,3,4,5]

第一步
1.所谓的闭开，就是指这个index能不能取到数
第二步：..

1.左闭右开的情况
    left = 0
    right = len(array) = 5
    那么在做right 不能 mid -1 while left < right

2.左闭右闭的情况
    left = 0
    right = len(array) - 1
    同时left,right = mid 加减 1，同时while left <= right:

3.最好的写法是左开右开(最健壮)
left = -1
right = len(array)
然后 left ,right 都等于mid ，同时while left + 1 != right:
"""
#1
def normal_binarysearch1(array, target):
        left = 0
        right = len(array)
        while left < right:
            mid = (left+right)//2
            print(mid)
            if array[mid] == target:
                return True
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid
        return False

#2 这种写法已经作为了我的通用模版，别的可以不看了
def normal_binarysearch2(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2

        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right -= 1
        else:
            left += 1

    return -1
"""
找的到的话，left,right 的数都是不确定的
找不到的话。left应该在区间的右边，right在区间的左边
例如：
[-1,0,3,5,9,12] 找出来,循环结束后，left = 3, right = 2
4
"""

# 3
def normal_binarysearch3(array, target):
    left = -1
    right = len(array)


    while left + 1 != right:
        mid= (left + right) // 2

        if array[mid] == target:
            return True
        elif array[mid] < target:
            left = mid
        else:
            right = mid
    return False



#测试：https://leetcode.com/problems/binary-search/submissions/
if __name__ == "__main__":
    print(normal_binarysearch1([2,3,4,5,6,7],7))
    print(normal_binarysearch1([2, 3, 4, 5, 6, 7], 2))
    print(normal_binarysearch1([2, 3, 4, 5, 6, 7], 3))
    print(normal_binarysearch1([2, 3, 4, 5, 6, 7], 4))
    print(normal_binarysearch1([2, 3, 4, 5, 6, 7], 5))
    print(normal_binarysearch1([2, 3, 4, 5, 6, 7], 6))

    print("--------false---------------")
    print(normal_binarysearch1([2, 3, 4, 5, 6, 7], 0))
    print(normal_binarysearch1([2, 3, 4, 5, 6, 7], 11))
    print(normal_binarysearch1([2, 3, 4, 6, 7], 5))
    # print(normal_binarysearch1([2, 3, 4,  6, 7], 4.5))