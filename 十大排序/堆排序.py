
def swap(array, i , j):
    array[i], array[j] = array[j], array[i]

#// Time: O(log(n))
# 然后在这个
def siftDown(array, i, end):
    parent = i
    child = 2 * parent + 1

    while chile < end:
        #看哪个孩子节点比较大，就把child定位到那里，方便后面放上去
        if child + 1 <= end and array[child] < array[child+1]:
            child += 1

        #假如说parents已经大于最大的孩子节点，说明已经不用进行换位操作了
        if array[parent] > array[child]: break

        # 假如孩子节点真的大与parent,则换位，换位后，检查更下面的节点
        # 例如在最顶层更换的节点，那么就要检查下面的节点是不是也满足最大堆的条件
        swap(array, parent, child)
        parent = child
        child = 2 * parent + 1

def buildMaxHeap(array, end):
    #heapsort 都是从中位数元素开始的
    for i in range(end//2, -1, -1):
        siftDown(array, i, end)

#// Time: O(n*log(n)), Space: O(1)
def sort(array):
    if not array or len(array) == 0: return
    # 这一步把最大堆创建好
    buildMaxHeap(array, len(array)-1)

    #因为最顶的元素一定是最大的，所以我们每次把最顶的元素都与最后一个元素交换
    #元素变成从小到大排列
    for end in range(len(array)-1 ,0 ,-1):
        swap(array, 0, end)
        siftDown(array, 0, end-1)

"""
https://algocasts.io/series/sorting-algorithms/episodes/jwmBqnW8
堆排序的原理就是，从倒数第二层的最右节点开始heapify, 往左再往上
例如数组 6,5,3,1,8,7， 他就是取 len(array)/2 = 2, 第二个index开始进行heapify
然后2，1，0


这里利用了一个思想，如何把一位数组当作一个二叉树来进行操作
例如 6,5,3,1,8,7
可以变成
          6(0)
    5(1)       3(2)
 1(3) 8(4)   7(5)

父节点下标    子节点下标
0             1，2         
1             3，4
2             5，6
i            2i+1, 2i+2
(i-1)/2          i    
"""
