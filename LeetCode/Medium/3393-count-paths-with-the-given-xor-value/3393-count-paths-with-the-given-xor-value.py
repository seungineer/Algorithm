class Solution:
    def countPathsWithXorValue(self, grid: list[list[int]], k: int) -> int:
        MOD = int(1e9 + 7)
        N = len(grid)
        M = len(grid[0])
        dp = [[[0 for _ in range(16)] for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if i == 0 and j == 0:
                    dp[i][j][grid[i][j]] += 1
                    continue
                if i - 1 < 0 and j - 1 >= 0:
                    for el in range(16):
                        res = el ^ grid[i][j]
                        dp[i][j][res] += dp[i][j-1][el] % MOD
                    continue
                if i - 1 >= 0 and j - 1 < 0:
                    for el in range(16):
                        res = el ^ grid[i][j]
                        dp[i][j][res] += dp[i-1][j][el] % MOD
                    continue
                for el in range(16):
                    res = el ^ grid[i][j]
                    dp[i][j][res] += dp[i-1][j][el] % MOD
                    dp[i][j][res] += dp[i][j-1][el] % MOD
        return (dp[-1][-1][k] % MOD)
                    