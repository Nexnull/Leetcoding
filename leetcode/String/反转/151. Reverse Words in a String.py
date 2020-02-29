"""
Given an input string, reverse the string word by word.
（按照单词来进行反转，但是要注意忽略掉前面的空格）
Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
"""


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s and len(s) == 0: return s
        string = list(s)

        p = 0; q = 0; end = len(string) - 1
        while end >= 0 and string[end] == " ": end -= 1

        while q <= end:
            start = p
            while q <= end and string[q] == " ": q += 1
            while q <= end and string[q] != " ":
                #起到一个把新字符串首尾的空格消除的作用
                string[p] = string[q]
                p += 1
                q += 1
            self.reverse(start, p - 1, string)
            if q <= end:
                string[p] = " "
                p += 1

        self.reverse(0, p - 1, string)
        return "".join(string[:p])

    def reverse(self, start, end, string):
        while start < end:
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1

"""
https://algocasts.io/episodes/BPp63kWr
// Time: O(n), Space: O(n)
答案：
1.首先处理corner case
2.创建一个string的list, p代表新string的指针，q代表旧string的指针
他们两个都在string上遍历，替换是inplace的
3.先把string后面的空格给去掉，用end --
4.然后就可以开始while q <= end: 开始把开头的空格去掉，用q++
5.当q到达正主的时候（单词），开始和p进行inplace赋值
6.附值在q遇到空格是停止，那是单词中间的间隙，这时候要开始reverse新附值的单词了【start,p-1]
7.把单词反转过后，加上空格，重复5-7的过程
8.所有单词反转过之后，最后整体再反转一遍，得到结果

例子 "apple care"
     elppa  erac(先把每个单词反转一遍)
     care apple（最后整体反转一遍）得到结果

"""










