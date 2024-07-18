class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        h_cnt = 1
        v_cnt = 1
        tot = 0
        horizontalCut.sort()
        verticalCut.sort()
        while horizontalCut or verticalCut:
            max_h = 0
            max_v = 0
            if horizontalCut:
                max_h = horizontalCut[-1]
            if verticalCut:
                max_v = verticalCut[-1]
            if max_v > max_h: # 세로 반갈 비용이 더 클 때
                tot += h_cnt * max_v
                v_cnt += 1
                # max_v_idx = verticalCut.index(max_v)
                verticalCut.pop()
            else:
                tot += v_cnt * max_h
                h_cnt += 1
                # max_h_idx = horizontalCut.index(max_h)
                horizontalCut.pop()
        return(tot)    