class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        start = points[0]
        points.remove(start)
        cnt = 0
        i = 0
        while i <= len(points)-1:
            if abs(start[0] - points[i][0]) >= 1 and abs(start[1] - points[i][1]) >= 1:
                cnt += 1
                if start[0] - points[i][0] < 0:
                    start[0] += 1
                else:
                    start[0] -= 1

                if start[1] - points[i][1] < 0:
                    start[1] += 1
                else:
                    start[1] -= 1
            elif abs(start[0] - points[i][0]) >= 1:
                cnt += 1
                if start[0] - points[i][0] < 0:
                    start[0] += 1
                else:
                    start[0] -= 1
            elif abs(start[1] - points[i][1]) >= 1:
                cnt += 1
                if start[1] - points[i][1] < 0:
                    start[1] += 1
                else:
                    start[1] -= 1
            else:
                start[0] = points[i][0]
                start[1] = points[i][1]
                i+=1
        return(cnt)