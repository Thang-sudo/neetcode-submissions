class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # x and y are the coordinator
        # i is the character of 'word' we're comparing with
        # if word[i] == board[x][y] and i == len(word) - 1 => True, found it
        # if word[i] != board[x][y] => False stop looking further
        # if word[i] == board[x][y] and i < len(word) - 1 -> more to compare then recursively search left, right, up, down to compare word -> mark the current cell as "#" so we dont accidentally revisit. If the current path doesn't result in the word then we should backtrack and search a different path. While doing so, we should revert the "#" character
        mark = "#"
        def search(x: int, y: int, i: int) -> bool:
            if word[i] == board[x][y] and i == len(word) - 1:
                return True
            elif word[i] != board[x][y]:
                return False
            elif word[i] == board[x][y] and i < len(word) - 1:
                # mark the path, so we wont revisit it
                temp = board[x][y]
                board[x][y] = mark
                # search left (x - 1, y)
                left, right, up, down = False, False, False, False
                if x > 0 and board[x - 1][y] != mark:
                    left = search(x - 1, y, i + 1)
                # search right (x + 1)
                if x < len(board) - 1 and board[x + 1][y] != mark:
                    right = search(x + 1, y, i + 1)
                # search up (y - 1)
                if y > 0 and board[x][y - 1] != mark:
                    up = search(x, y - 1, i + 1)
                # search down (y + 1)
                if y < len(board[x]) - 1 and board[x][y + 1] != mark:
                    down = search(x, y + 1, i + 1)
                # unmark after searching all directions
                board[x][y] = temp
                if left or right or up or down:
                    return True
                else:
                    return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if search(i, j, 0):
                    return True
        return False
