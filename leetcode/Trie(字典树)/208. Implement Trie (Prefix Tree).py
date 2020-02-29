"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
写一个字典树
"""


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            node = node.setdefault(char,{})
        node[self.end_of_word] = self.end_of_word


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

if __name__ == "__main__":
    solution = Trie()
    solution.insert("apple")
    print(solution.root)

    boo = {}
    new = boo
    new.setdefault("a",{})
    for char in "apple":
        new = new.setdefault("a",{})
    print(boo)
"""
https://www.youtube.com/watch?v=TkR3CbEh0Ag&lis=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=38
答案：
1.insert 的那个写法把我给看懵了，为什么这样循环写就可以写出来？？？
2. 找的时候是一个字母一个字母，一层一层得往下找，假如没找到retrun False
假如循环结束，但是没有找到单词的结束标志"#"，说明单词没找完，return False
3.只找部分的话其实就很好找了，其实跟第二步一样，只不过不用验证最后是否存在"#"


"""