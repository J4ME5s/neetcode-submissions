class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # loop through all possible first letter
        # Choices: Right or Down
        rows = len(board)
        cols = len(board[0])
        
        def dfs(row: int, col: int, i: int):
            if i == len(word):
                return True
            
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return False
            
            if board[row][col] != word[i]:
                return False
            
            curr = board[row][col]
            board[row][col] = "#" # mark it as visited

            found = (
                dfs(row - 1, col, i + 1) or
                dfs(row + 1, col, i + 1) or
                dfs(row, col - 1, i + 1) or
                dfs(row, col + 1, i + 1)
            )
            board[row][col] = curr # unmark

            return found
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, 0):
                    return True
        return False

