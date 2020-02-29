"""
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
#hash map的做法
class Solution(object):
    def groupAnagrams(self, strings):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strings or len(strings) == 0: return []

        hashmap = {}

        for string in strings:
            key = self.getkeybySort(string)

            if key not in hashmap.keys():
                hashmap[key] = [string]
            else:
                hashmap[key].append(string)

        return list(hashmap.values())


    def getkeybySort(self,word):
        word = list(word)
        word.sort()
        return "".join(word)

    def getkeybyCount(self,word):
        res = [0]*26
        for char in word:
            res[ord(char) - ord("a")] += 1
        return tuple(res)


"""   
Time: O(n*k*log(k)), Space: O(n) ,k为单词长度，用排序做key
      O(n*k) space:O(n) 用数组计数
答案:
1.我们先把每个单词排序好，那么所有变位词的排序好都是好一样的，用处理好的变位词做key
                                                       用单词的原始形态做value，用[]储存

2.关于获取这个key，有两种做法
  2.1 第一种就是把这个单词给排序好，因为变位词排序好之后都是一样的，可以用这个做key，O(klogk)
  2.2 第二种就是把就是把一个单词的字母出现次数记录在list里，然后用这个字母出现次数来做key
  能节省时间复杂度，因为遍历一次只需要 O(n)
  
2.我们所要做的就是一个简单的hash 输入输出的操作
"""