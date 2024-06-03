class Solution:
    def minimumLines(self, stockPrices: list[list[int]]) -> int:
        n = len(stockPrices)
        stockPrices.sort()
        if n == 1:
            return 0
        if n == 2:
            return 1
        x1, y1 = stockPrices[0][0], stockPrices[0][1]
        x2, y2 = stockPrices[1][0], stockPrices[1][1]
        dy1= (y2 - y1)
        dx1 = (x2 - x1)
        cnt = 1
        for i in range(2, n):
            x2, y2 = stockPrices[i][0], stockPrices[i][1]
            dy2 = (y2 - y1)
            dx2 = (x2 - x1)
            if dy1*dx2 == dy2*dx1:
                continue
            else:
                x1, y1 = stockPrices[i-1][0], stockPrices[i-1][1]
                dy1= (y2 - y1)
                dx1 = (x2 - x1)
                cnt += 1
        return cnt