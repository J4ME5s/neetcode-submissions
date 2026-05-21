class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        i = 0
        for i in range(len(board)):
            j = 0
            newSet = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in newSet:
                        return False
                    newSet.add(board[i][j])

        # check columns
        j = 0
        for j in range(len(board)):
            i = 0
            newSet = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in newSet:
                        return False
                    newSet.add(board[i][j])

        # check boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                boxSet = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != ".":
                            if board[i][j] in boxSet:
                                return False
                            boxSet.add(board[i][j])
                col += 3
            row += 3
        
        return True
