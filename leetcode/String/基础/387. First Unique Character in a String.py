"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
Examples:

s = "leetcode"
return 0.
s = "loveleetcode",
return 2.
"""
from sys import maxsize
class Solution(object):
    def firstUniqChar(self, string):
        """
        :type string: str
        :rtype: int
        """
        if not string or len(string) == 0: return -1

        count = [0] * 26
        pos = [0] * 26

        for i in range(len(string)):
            index = ord(string[i]) - ord("a")
            count[index] += 1
            if pos[index] == 0: pos[index] = i

        first_pos = maxsize
        for i in range(len(pos)):
            if count[i] == 1:
                first_pos = min(first_pos, pos[i])

        return -1 if first_pos == maxsize else first_pos

"""
利用了hash map
https://algocasts.io/episodes/Y9pJkYWA
采取了最优解的做法，所以理解起来会稍微有点难度
Time O(n) space: O(n)
答案：
1.count是一个hash map,对应的是字母出现的次数
  pos也是一个hash map,对应的是字母第一次出现时的位置
  
2.所以我们遍历整个string, 把每个字母在26字母中对应的位置求出来(index)
  然后把它的出现的次数++
  假如说这个字母是第一次出现（pos[index] = 0）,那么就让pos[index] = i（这个字母在string的位置）

3.从1-26遍历
    我们只看count[i] == 1(只出现过一次的字母)。
    把第一在string 出现的最前的一个字母的index 找出来

4.假如说first_pos没有更新，说明没有字母只出现过一次，返回-1
  否则返回 first_pos

优化点：
1。正常的hash map,我们遍历一遍string,把每个字母出现多少次找出来，
  然后再遍历一次string,把count[index]==1的字母找出来。
  假如string 很大的话，worst case可能会变得很大 O(len(string)^2)
   
2。所以我们的做法是等于是 O(len(string)*26)

"""
        
        
        

