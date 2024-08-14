class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        i = 0 # 행
        j = 0 # 열
        for k in commands:
            if k == "RIGHT":
                if j + 1 < n :
                    j += 1
            elif k == "LEFT":
                if 0 <= j - 1:
                    j -= 1
            elif k == "UP":
                if 0 <= i - 1:
                    i -= 1
            elif k == "DOWN":
                if i - 1 < n:
                    i += 1
        return (i*n)+j
        