
def quickSort(array: list, low: int, high: int) -> int:
    if low < high:
        #找出分界点pivot
        pi = partition(array, low , high)

        #利用分界点把原数组分成两半，对每一半都进行排序
        quickSort(array, low , pi-1)
        quickSort(array, pi+1, high)

#真正的排序在这个函数
def partition(array , low , high):
    pivot = high
    slow = low
    fast = low
    while fast < high:
        # 大于pivot的不用管，小于pivot的要和slow换位
        if array[fast] < array[pivot]:
            swap(array, slow , fast)
            slow += 1
        fast += 1

    # 当j走到最后的时候（pivot)所在位置，要和i交换一下，把pivot放在合适的位置（i）
    swap(array, slow, fast)
    # i的位置现在放的是pivot,左边的数比pivot小，右边的数比pivot大
    return slow

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def main(array):
    if not array or len(array) == 0:
        return []
    quickSort(array,0,len(array)-1)
    print(array)

main([5,4,3,2,1])
"""
https://algocasts.io/episodes/kVG9Pxmg
"""
