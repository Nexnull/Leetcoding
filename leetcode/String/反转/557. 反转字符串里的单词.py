class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        char = list(s)
        # start指向单词的第一个字母， end用来指向单词的最后一个字母
        start = end = 0

        while start < len(char):
            # 目的是让end 移动到单词的后一位
            while end < len(char) and char[end] != " ":
                end += 1

            # 因为end 在单词的后一位，所以index上要-1， 使得i,j分别指向单词头和单词尾
            self.swap(char, start, end - 1)
            start = end + 1
            end = start

        return "".join(char)

    def swap(self, array, i, j):
        while i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

"""
Time: O(n), Space: O(n)
https://algocasts.io/episodes/j5pgPlWx

"""