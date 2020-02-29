# coding=utf-8
import sys
def expend_helper(string, index):
    odd = expend(string, index, index) - 1
    even = expend(string, index, index + 1)
    return max(odd, even)

def expend(string, left, right):
    res = 0
    while string[left] == string[right] and left > -1 and right < len(string):
        left -= 1
        right += 1
        res += 2
    return res

def q1(string):
    if not string: return None
    res = 0
    for i in range(len(string)):
        cur = expend_helper(string, i)
        if cur > res:
            res = cur
    return res

if __name__ == "__main__":
    data = []

    while True:
        line = sys.stdin.readline().strip()
        if not line: break
        data.append(line)

    print(q1(data[0]))
