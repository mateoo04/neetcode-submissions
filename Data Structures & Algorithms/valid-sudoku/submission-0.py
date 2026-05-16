import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == ".": continue
                if (board[x][y] in rows[x]) or (board[x][y] in columns[y]) or (board[x][y] in squares[str(x//3)+str(y//3)]): return False
                else:
                    rows[x].add(board[x][y])
                    columns[y].add(board[x][y])
                    squares[str(x//3)+str(y//3)].add(board[x][y])
                    print("squares: ", squares)

        return True


        