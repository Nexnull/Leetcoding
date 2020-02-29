"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution(object):
    def partition(self, string):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not string and len(string) == 0: return []
        self.res = []
        self.dfs(string,[])
        return self.res

    def dfs(self,string,temp):
        # 终止条件，当指针i查到最后了，这样返回不出string,就说明已经遍历完了
        if not string:
            self.res.append(temp[:])
            return

        # backtracking
        # 我们把当前位置的字符串，一次次分层例如aab,我们分层a,然后切分找后面的结果
        #                                    再分成aa,然后切分找后面的结果
        for i in range(1,len(string)+1):
            if self.isPalis(string[:i]):
                temp.append(string[:i])
                self.dfs(string[i:],temp)
                temp.pop(-1)

    def isPalis(self,string):
        return string == string[::-1]

"""
https://www.youtube.com/watch?v=UFdSC_ml4TQ
"""