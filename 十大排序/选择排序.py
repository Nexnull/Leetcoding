
def swap(array, i, j):
    array[i] , array[j] = array[j], array[i]


def selectionSort(array):
    if not array or len(array) == 0: return None
    n = len(array)

    for i in range(n):
        minidx = i
        for j in range(i+1,n):
            if array[j] < array[minidx]:
                minidx = j
        swap(array, i, minidx)


