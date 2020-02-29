"""
Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
注意这里是less than n,就是假如说n = 7，那么质数取不到7
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:return 0
        res = [True]*n
        res[0] = False
        res[1] = False

        for i in range(int(n**0.5)+1):
            if res[i] == True:
                for j in range(i*i,n,i):
                    res[j] = False
        return sum(res)

"""
空间法度 O（n），时间法度O（nloglogn)
https://www.youtube.com/watch?v=UGeCe5WQNVg
答案：
1.首先我们创建一个记录数组res,假设上面的每一个index对应现实中的每一个数字
True表示它是质数，False表示它不是质数
2.我们知道0,1不是质数
3.然后我们让i遍历到 n^0.5，因为根据后面的情况来看，遍历到那里已经足够了
4.当res[i] = Ture,我们要以这个数为基础，把他的倍数都变成False
5.最后返回res里true的个数，用sum（）来计算

注意：
1.这里是要求找less than n的质数，所以我们只需要从[0,n-1]找到这里面的质数就行了，所以res.length = n
2.第二个for循环，一定要从i*i，或2*i也可以 开始往前找，因为假如说for (i ,n,i),那么原来为质数的[i]
会变成false，导致错误
"""
