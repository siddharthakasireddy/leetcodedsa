class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            for nei in range(n):
                if isConnected[city][nei] == 1 and not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        provinces = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                provinces += 1

        return provinces

        