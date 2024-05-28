class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        def mergeorpass(intervals, i):
            if len(intervals) == 1:
                return intervals

            if intervals[i][-1] >= intervals[i+1][0]: # 오버랩 시
                if intervals[i][-1] <= intervals[i+1][-1]:
                    intervals[i] = [intervals[i][0], intervals[i+1][-1]]
                intervals.remove(intervals[i+1])
                i -= 1
                return i
            return i
        intervals.sort()
        i = 0
        while True:
            if len(intervals) == i+1:
                break
            i = mergeorpass(intervals, i)
            i += 1

        return intervals
