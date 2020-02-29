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
        nums = ["1","2","3","4","5","6","7","8","9"]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    for c in nums:
                        if self.isvalid(board,i,j,c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True



    def isvalid(self, board, row, col, c):
        for i in range(9):
            if board[i][col] != "." and board[i][col] == c:return False
            if board[row][i] != "." and board[row][i] == c: return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3] != "." and \
                board[3*(row//3)+i//3][3*(col//3)+i%3] == c:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValidSudoku(
        [[".","8","7","6","5","4","3","2","1"],
         ["2",".",".",".",".",".",".",".","."],
         ["3",".",".",".",".",".",".",".","."],
         ["4",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".",".","."],
         ["6",".",".",".",".",".",".",".","."],
         ["7",".",".",".",".",".",".",".","."],
         ["8",".",".",".",".",".",".",".","."],
         ["9",".",".",".",".",".",".",".","."]]
 ))

"""
https://www.youtube.com/watch?v=2FV8tgBCYqI&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=34
作为求解数独的复杂版，我们要在空格处填满所需要的字符
1。遍历每个节点
2。创立一个1-9的list，我们需要用这九个数字"。"里套，看哪个数字可以用
3。当节点为"。"的时候我们开始套1-9，同时检查"。"套进一个数字 c 后，是否符合数独规则
4。在 isvalid（）里面检查套进的元素c，是否满足横，竖，九宫格无相同
5。当前情况没问题后，就把c 放在[i][j]上
6。递归，再调用一次solve（），在c被放置的基础上，继续放置别的元素，重复1-5的循环

7.假如一直放置都很成功，递归到头，重重回调，return True
8.假如在途中有c 放置不成功的，solve（）return false,那么我们要把上一个递归的[i][j]给还原成"。"，然后再尝试别的
c

9。假如说一切顺利结束，return true。
假如说一路不顺利，那么在第一次递归的时候就会失败，返回false.第一个递归返回false.就意味着整个程序返回false
失败



注意：这里利用了修枝，当循环进入到有。的时候，我们直接跳过，节省了时间
"""