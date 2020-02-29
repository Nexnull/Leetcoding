"""
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or len(board) == 0 or not board[0] or len(board[0]) == 0:
            return False
        m = len(board) ; n = len(board[0])
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if self.is_exist(board,word,i,j,0,visited):
                    return True
        return False



    def is_exist(self, board , word , i , j , index, visited):
        if index == len(word): return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or \
            visited[i][j] == True or board[i][j] != word[index]:
            return False
        visited[i][j] = True
        seek = self.is_exist(board,word,i+1,j,index+1,visited) or \
               self.is_exist(board, word, i - 1, j, index + 1, visited) or \
               self.is_exist(board, word, i , j + 1, index + 1, visited) or \
               self.is_exist(board, word, i, j - 1, index + 1, visited)
        visited[i][j] = False
        return seek

"""

答案：
1.visited是用来记录当前这个点在本次查找中是否被访问过，如果被访问过
则为True,没有则是False
2.然后剩下的就没啥难的，无非是所有节点遍历，然后DFS
3.helper函数注意要传一个index
3.在index越界，或者word[index]和word[i][j]不同时，返回False
4.判断没问题，就把visited[i][j] == True, 然后dfs, dfs完后visited[i][j] == False
"""