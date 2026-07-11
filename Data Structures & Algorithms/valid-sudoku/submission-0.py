class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]
        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == ".":
                    continue
                box = r // 3 * 3 + c // 3
                if char in rows[r] or char in cols[c] or char in squares[box]:
                    return False
                rows[r].add(char)
                cols[c].add(char)
                squares[box].add(char)
        return True