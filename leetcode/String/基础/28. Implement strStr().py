"""
Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and needle:return -1
        if not needle:return 0


        n = len(haystack)
        m = len(needle)

        for i in range(n-m+1):
            k = i
            j = 0
            while k < n and j < m and haystack[k] == needle[j]:
                k += 1
                j += 1
            if j == m:return i

        return -1

"""
Time:O(n * m) Space:O(1)
双指针的做法
答案：
0.先限定查找范围，具体看2.0，查找范围为[0,len(haystack) - len(needle)]
1.定下两个指针，一个是k,k在haystack上走
              另一个是j，j是在needle上走
    每次检查是否：haystack[k] == needle[j],满足的话k++,j++
2.假如说j 移动到列表的最末端+1了，说明needle的连续元素在haystack都能连续的找到，
返回index i（标准连续字符串相同的起始位置）

1.这题的corner case需要考虑下，因为我们是要看needle是否在haystack里面
所以假如说needle 为""，那么正确
假如说haystack没有，needle有，那么错误
2.细节：假如说h = abcde , n = cde , len(h)- len(n) = 2
  我们是需要判断h的前三个存不存在n的第一个元素
  所以这里我们需要range(len(h)- len(n) + 1)
3.细节: 这里的双指针遍历,我们不能用i 和 j。因为i是用来记录在haystack里的第几个位置开始出现重复，而k,j假如说匹配的话，他们会一直遍历到needle的末index。
  所以我们要创建 i , j,k三个指针
"""


