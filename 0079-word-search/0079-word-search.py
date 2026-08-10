class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, index):

            # All characters found
            if index == len(word):
                return True

            # Check boundaries and character
            if (row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] != word[index]):
                return False

            # Mark the cell as visited
            temp = board[row][col]
            board[row][col] = '#'

            # Search in four directions
            found = (
                dfs(row + 1, col, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row, col - 1, index + 1)
            )

            # Restore the cell
            board[row][col] = temp

            return found

        # Try every cell as the starting point
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False