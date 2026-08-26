class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # How to calculate box index
        # First take col // 3, row // 3 to find which box the element belongs to
        # This make original sudoku elements fit into a matrix like this:
        # (0, 0), (0, 1), (0, 2)
        # (1, 0), (1, 1), (1, 2)
        # (2, 0), (2, 1), (2, 2)
        # However, we want this to become an index to track
        # (row // 3) * 3 + (col // 3)
        # (row // 3) * 3 because every 3 box, we reach a new row
        # + (col // 3) = add the column offset
        # Turn original matrix into this
        # (0), (1), (2)
        # (3), (4), (5)
        # (6), (7), (8)

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
                    
