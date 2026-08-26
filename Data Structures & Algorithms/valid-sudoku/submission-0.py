class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in rows[i]:
                    rows[i].add(board[i][j])
                else:
                    return False
        for i in range(0, 9):
            for j in range(0, 9):
                if board[j][i] == ".":
                    continue
                if board[j][i] not in cols[i]:
                    cols[i].add(board[j][i])
                else:
                    return False
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                square_index = (i // 3) * 3 + (j // 3)
                if board[i][j] not in squares[square_index]:
                    squares[square_index].add(board[i][j])
                else:
                    return False
        return True
                    
