"""
Each word must be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring. (重要)
The same letter cell may not be used more than once in a word.（重要）

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
"""
import collections

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
end_of_word = "#"
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not words:return []
        self.res = set()

        #这里为正常的字典树添加元素的过程，参考208
        root = collections.defaultdict()
        for word in words:
            #这里node = self.root有什么位置上的讲究吗
            node = root
            for char in word:
                node = node.setdefault(char,collections.defaultdict())
            node[end_of_word] = end_of_word

        self.n = len(board)
        self.m = len(board[0])

        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] in root:
                    self.dfs(board , i , j , "" , root)
        return self.res

    def dfs(self,board , i, j ,cur_word , cur_dict ):

        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]

        if end_of_word in cur_dict:
            self.res.add(cur_word)

        # @表示当前这个ij位置的数正在被使用中
        temp , board[i][j] = board[i][j] , "@"

        for k in range(4):
            x , y = i + dx[k] , j + dy[k]
            if 0 <= x <self.n and 0<= y < self.m \
                and board[x][y] != "@" and board[x][y] in cur_dict:
                self.dfs(board,x,y,cur_word,cur_dict)
        board[i][j] = temp

if __name__ == "__main__":
    solution = Solution()
    solution.findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
],["oath","pea","eat","rain"])

"""
https://www.youtube.com/watch?v=IkoDuL2vD6A&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=39
答案：


"""