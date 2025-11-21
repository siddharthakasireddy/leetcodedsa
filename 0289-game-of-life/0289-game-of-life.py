class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        rows, cols = len(board), len(board[0])
        
        # 8 directions
        directions = [
            (1,0), (-1,0), (0,1), (0,-1),
            (1,1), (1,-1), (-1,1), (-1,-1)
        ]
        
        def live_neighbors(r, c):
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # abs(board[nr][nc]) == 1 → originally live
                    if abs(board[nr][nc]) == 1:
                        count += 1
            return count
        
        # First pass: apply rules with encoding
        for r in range(rows):
            for c in range(cols):
                lives = live_neighbors(r, c)
                
                # Rule 1 or 3: Live cell dies -> mark as -1
                if board[r][c] == 1 and (lives < 2 or lives > 3):
                    board[r][c] = -1
                    
                # Rule 4: Dead cell becomes live -> mark as 2
                if board[r][c] == 0 and lives == 3:
                    board[r][c] = 2
        
        # Second pass: finalize the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0

        