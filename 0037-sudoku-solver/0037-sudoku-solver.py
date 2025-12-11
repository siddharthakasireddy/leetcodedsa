class Solution(object):
    def solveSudoku(self, board):

        # Hash sets to track used numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize sets and record empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    box_id = (r // 3) * 3 + (c // 3)
                    boxes[box_id].add(val)

        def backtrack(i):
            # If all empty cells are filled → solved
            if i == len(empty):
                return True

            r, c = empty[i]
            box_id = (r // 3) * 3 + (c // 3)

            for ch in "123456789":
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_id]:
                    # Place the digit
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box_id].add(ch)

                    # Continue to next empty cell
                    if backtrack(i + 1):
                        return True

                    # Undo on failure
                    board[r][c] = '.'
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box_id].remove(ch)

            return False

        backtrack(0)


        