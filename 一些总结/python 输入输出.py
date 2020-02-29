
import sys

if __name__ == "__main__":
    data=[]
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        data.append(line.split())
    # 数字的转换成数字以及数字的做法
    # target = int(data[0].strip())
    # nums = list(map(int,data[1].split(" ")))
    # print(data, target, nums)

    # 转换成字符串的的做法
    # target = "".join(data[0])
    # string = "".join(data[1])

    print(data)

"""
https://blog.csdn.net/sunlanchang/article/details/99825347
https://blog.csdn.net/qq_39283195/article/details/90577000我参考的是下面这个
"""
