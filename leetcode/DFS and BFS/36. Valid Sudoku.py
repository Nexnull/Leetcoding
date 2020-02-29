class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board == None or len(board) == 0:
            return
        return self.solve(board)


    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                else:
                    if self.isvalid(board,i,j,board[i][j]):
                        continue
                    return False
        return True

    def isvalid(self, board, row, col, c):
        for i in range(9):
            if  board[i][col] == c and i != row:return False
            if  board[row][i] == c and i != col:return False
            #[1,2,3]
            #[4,5,6]
            #[7,8,9]
            if (3 * (row // 3) + i // 3) == row and  3 * (col // 3) + i % 3 == col:
                continue
            else:
                if board[3*(row//3)+i//3][3*(col//3)+i%3] == c:
                    return False
        return True




"""
作为求解数独的简单版，我们只要检查数独中的数字是否满足数独的规定就好了
1。遍历每个节点
2。当节点为"。"的时候跳过，当节点为数字的时候检查横竖，以及九宫格内是否满足无重复数字
3。这个检查的函数写的有点水平，已知 row , col都是不变的，我们只需要移动它的纵坐标和横坐标（改变i）
    需要注意当遍历到自己位置的元素时，需要跳过
4。3 * (row // 3) + i // 3。
   3 * (row // 3)，定下row所在区位的最小值，例如row为3，结果为0
   但row 的变化范围为1-3，是由i//3来控制（除法分数向下取整），变化速率慢
5。同理3 *(col//3) + i % 3。左边是控制col所在区间的最小值，例如col = 5,结果为3
    row 的变化范围也是由 i%3来控制的，变化速率快
    
    例如row , col = 3,3
    则结果为 33 34 35 43 44 45 53 54 55
注意：这里利用了修枝，当循环进入到有 "。" 的时候，我们直接跳过，节省了时间
"""