def merge(left,right):
def merge(left,right):
    l = 0
    r = 0
    result = []
    while l<=len(left)-1 and r <= len(right)-1:
        if left[l] < right[r]:
            result.append(left[l])
            l += 1

        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]
    return result


def mergesort(data):
    if len(data) == 1:
        return data


    middle = len(data)//2
    left = mergesort(data[:middle])
    right = mergesort(data[middle:])


    return merge(left,right)

mergesort([5,4,3,2,1])