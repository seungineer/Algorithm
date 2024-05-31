from collections import deque
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n = len(grid[0]) # 너비
        m = len(grid) # 높이
        wait_list = deque()
        def dfs(i, j):
            grid[i][j] = "0"
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                if nx >= n or nx < 0 or ny < 0 or ny >= m:
                    continue
                if grid[ny][nx] == "1":
                    dfs(ny, nx)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1
        print(grid)
        print(cnt)
        return cnt