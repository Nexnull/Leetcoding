"""
这里来对比寻找旋转数组的最大值和最小值
"""

def findMax(nums):
    if not nums:
        return
    left = 0
    right = len(nums) - 1
    while left < right:  # left >= right 退出
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid
        else:
            right = mid - 1
    return nums[left]


def findMin(nums):
    if not nums:
        return
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left + right) //2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

"""
我们可以发现，主要不同的地方在于，两个函数进行分区的方法不一样
findMax,要把指针移动到大递增区间（左边），我们分区就一定要用left,nums[left] < nums[mid]
findMin,
"""

print(findMax([4,5,6,7,0,1,2]))
print(findMax([4,5,6,0,1,2]))
print(findMax([4,5,6,7,7,0,1,2,3]))