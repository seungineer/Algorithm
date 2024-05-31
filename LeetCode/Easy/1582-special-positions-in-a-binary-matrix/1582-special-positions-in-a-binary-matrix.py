class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        m = len(mat[0]) # 너비
        n = len(mat) # 높이
        temp = []
        temp2 = []
        total = 0
        cnt = 0
        flag = False
        for i in range(n):
            temp.append(sum(mat[i]))
        for j in range(m):
            for i in range(n):
                total += mat[i][j]
            temp2.append(total)
            total = 0
        print(temp, temp2) # 행, 열
        for j in range(m): # 너비
            if temp2[j] == 1:
                for i in range(n): # 높이
                    if temp[i] == 1:
                        if mat[i][j] == 1:
                            cnt += 1

        return cnt