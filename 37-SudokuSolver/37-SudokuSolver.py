# Last Updated: 6/22/2026, 12:45:00 AM
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        empty=[]
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    empty.append((r,c))
                else:
                    ch=board[r][c]
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[(r//3)*3+c//3].add(ch)
        def backtracker(indx):
            if indx==len(empty):
                return True
            r,c=empty[indx]
            box=(r//3)*3+c//3
            for ch in '123456789':
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box]:
                    board[r][c]=ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box].add(ch)
                    if backtracker(indx+1):
                        return True
                    board[r][c]='.'
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box].remove(ch)
            return False
        backtracker(0)
                    
