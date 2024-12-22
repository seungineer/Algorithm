class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        x_axis = []
        y_axis = []
        for el in rectangles:
            st_x, st_y, en_x, en_y = el
            x_axis.append([st_x, 1])
            x_axis.append([en_x, -1])
            y_axis.append([st_y, 1])
            y_axis.append([en_y, -1])
        x_axis.sort()
        y_axis.sort()
        lines = 0
        stk = 0
        for i in range(len(x_axis)):
            x, point = x_axis[i]
            stk += point
            if stk == 0: lines += 1
            if lines == 3: break
        if lines == 3: return True
        
        lines = 0
        stk = 0
        for i in range(len(y_axis)):
            y, point = y_axis[i]
            stk += point
            if stk == 0: lines += 1
            if lines == 3: break
        if lines == 3: return True
        
        return False