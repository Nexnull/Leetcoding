class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0: return
        self.lrow = len(board)
        self.lcol = len(board[0])
        self.visited = [[False for j in range(self.lcol)] for i in range(self.lrow)]

        # check edge from up to down
        for i in range(0, self.lrow):
            if board[i][0] == "O":
                self.dfs(board, i, 0, False)
            if board[i][self.lcol - 1] == "O":
                self.dfs(board, i, self.lcol-1 , False)

        # check edge from left to right
        for j in range(0, self.lcol):
            if board[0][j] == "O":
                self.dfs(board, 0, j, False)
            if board[self.lrow - 1][j] == "O":
                self.dfs(board, self.lrow-1, j, False)

        # fipe the tile on the middle
        for i in range(1, self.lrow - 1):
            for j in range(1, self.lcol - 1):
                if board[i][j] == "O" and self.visited[i][j] == False:
                    self.dfs(board,i,j,True)



    def dfs(self, board, i, j, flip):
        if i < 0 or i > self.lrow - 1 or j < 0 or j > self.lcol - 1:
            return
        if board[i][j] == "X": return
        if self.visited[i][j]: return

        if flip: board[i][j] = "X"

        self.visited[i][j] = True
        self.dfs(board, i + 1, j, flip)
        self.dfs(board, i - 1, j, flip)
        self.dfs(board, i, j + 1, flip)
        self.dfs(board, i, j - 1, flip)

"""
https://www.youtube.com/watch?v=u0Xtggq0n10
答案：
思路其实挺简单的
1.谁不能被翻。四条边上的0,因为总有一面是围不上的，所以与最外围边0相连的0，都不可能被翻的
2.谁可以被翻。不在四条边上，且，没有与边上O相连的 O，可以被翻
3.dfs，我们要给它一个定性
  
  3.1 flip是从主函数传过来的，他也是会贯穿一整串dfs,例如是四周的O，那么，凡事四周O能
      连接到的O，flip都是false
      于此同时，走过的点，在dfs里会在self.visited里标记成True
      所以，一个点，在第一次遍历的时候，就决定了它翻不翻，以及，不能再遍历
  
  3.2 对于要翻的点也是一样，只有一次遍历，一次翻的机会
"""