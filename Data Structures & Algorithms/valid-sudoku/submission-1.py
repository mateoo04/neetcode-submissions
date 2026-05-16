import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == ".": continue
                row = str(board[x][y]) + " found in row " + str(x)
                col = str(board[x][y]) + " found in col " + str(y)
                square = str(board[x][y]) + " found in square " + str(x // 3) + str(y // 3)

                if(row in seen or col in seen or square in seen):
                    return False
                else:
                    seen.add(row)
                    seen.add(col)
                    seen.add(square)

        return True


        