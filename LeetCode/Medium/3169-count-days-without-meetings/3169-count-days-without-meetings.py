class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        i = 1
        while True:
            if i == len(meetings):
                break
            if meetings[i-1][1] >= meetings[i][0]: #역전 발생
                if meetings[i-1][1] >= meetings[i][1]: #(1,5 / 2,4)
                    meetings[i][0] = meetings[i-1][0]
                    meetings[i][1] = meetings[i-1][1]
                    meetings.remove(meetings[i-1])
                else:
                    meetings[i][0] = meetings[i-1][0]
                    meetings[i][1] = meetings[i][1]
                    meetings.remove(meetings[i-1])
            else: # 역전 발생 X
                i += 1
        scheduled = 0
        for lst in meetings:
            scheduled += lst[1] - lst[0] + 1
        return days - scheduled    