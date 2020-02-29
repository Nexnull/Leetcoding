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
答案：
1.来到这里，我们回溯的对象已经不是列表里的一个个元素了，而是一段又一段的字符串，我们要怎么处理回溯字符串的情况呢？
2.利用的是字符串的切片
3. 例如aab , 我们一开始切 a  ab, 先看a是不是回文的, 假如a是回文的，那我们把剩下的字符串放进helper
                   再切 aa b,  看aa是不是回文的， aa是回文的，把剩下的字符串放进helper
                    切 aab, aab不是回文的，所以直接略过
4.最后当传入helper的切片字符串为""的时候，说明前面的切片都是回文的，于是把答案加进res里面                    
"""