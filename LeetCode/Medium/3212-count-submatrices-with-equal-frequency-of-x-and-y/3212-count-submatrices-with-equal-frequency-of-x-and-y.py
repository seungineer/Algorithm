class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        col = len(grid[0])
        row = len(grid)
        res = [[[0,0] for _ in range(col+1)]for _ in range(row+1)]
        res2 = [[[0,0] for _ in range(col+1)]for _ in range(row+1)]
        cnt = 0
        for i in range(1,row+1):
            for j in range(1,col+1):
                if grid[i-1][j-1] == "X":
                    res[i][j][0] = res[i][j-1][0]
                    res[i][j][1] = res[i][j-1][1]
                    res[i][j][0] += 1
                elif grid[i-1][j-1] == "Y":
                    res[i][j][0] = res[i][j-1][0]
                    res[i][j][1] = res[i][j-1][1]
                    res[i][j][1] += 1
                else:
                    res[i][j][0] = res[i][j-1][0]
                    res[i][j][1] = res[i][j-1][1]

                res2[i][j][0] = res2[i-1][j][0]+res[i][j][0]
                res2[i][j][1] = res2[i-1][j][1]+res[i][j][1]
                if res2[i][j][0] == res2[i][j][1] and res2[i][j][0] >= 1:
                    cnt += 1

        return(cnt)    