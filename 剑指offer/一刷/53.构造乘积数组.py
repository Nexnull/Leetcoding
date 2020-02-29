
class Solution:
    def multiply(self, A):
        B = [1]*len(A)

        #计算上三角
        for i in range(1,len(A)):
            B[i] *= A[i-1]*B[i-1]

        #计算下三角
        temp = 1
        for j in range(len(A)-2,-1,-1):
            temp *= A[j+1]
            B[j] *= temp

        print(B)
        return B

if __name__ == "__main__":
    solution = Solution()
    solution.multiply([1,2,3,4,5,6])



"""
没啥太多的想法，硬乘的话就没啥意思了

答案：
<分析>：
解释下代码，设有数组大小为5。
对于第一个for循环
第一步：b[0] = 1;
第二步：b[1] = b[0] * a[0] = a[0]
第三步：b[2] = b[1] * a[1] = a[0] * a[1];
第四步：b[3] = b[2] * a[2] = a[0] * a[1] * a[2];
第五步：b[4] = b[3] * a[3] = a[0] * a[1] * a[2] * a[3];

然后对于第二个for循环
第一步
temp *= a[4] = a[4];
b[3] = b[3] * temp = a[0] * a[1] * a[2] * a[4];
第二步
temp *= a[3] = a[4] * a[3];
b[2] = b[2] * temp = a[0] * a[1] * a[4] * a[3];
第三步
temp *= a[2] = a[4] * a[3] * a[2];
b[1] = b[1] * temp = a[0] * a[4] * a[3] * a[2];
第四步
temp *= a[1] = a[4] * a[3] * a[2] * a[1];
b[0] = b[0] * temp = a[4] * a[3] * a[2] * a[1];

https://www.nowcoder.com/profile/9851815/codeBookDetail?submissionId=20707922
可以看这个图，说明了什么是下三角什么是上三角
"""