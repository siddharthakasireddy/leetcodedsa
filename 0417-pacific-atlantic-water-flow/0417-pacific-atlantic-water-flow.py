class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited):
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < m and 0 <= nc < n and
                    not visited[nr][nc] and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        # Pacific Ocean (top row & left column)
        for i in range(m):
            dfs(i, 0, pacific)
        for j in range(n):
            dfs(0, j, pacific)

        # Atlantic Ocean (bottom row & right column)
        for i in range(m):
            dfs(i, n - 1, atlantic)
        for j in range(n):
            dfs(m - 1, j, atlantic)

        # Cells reachable by both oceans
        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])

        return result

        