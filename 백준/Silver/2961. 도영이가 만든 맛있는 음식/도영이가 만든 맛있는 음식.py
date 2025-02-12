def solution():
    N = int(input())
    seq = [list(map(int, input().split())) for _ in range(N)]
    
    minDiff = [int(1e9)]
    def bt(tasteA, tasteB, idx): # 신맛, 쓴맛, 기 반영 위치
        minDiff[0] = min(minDiff[0], abs(tasteB - tasteA))

        for i in range(idx+1, N):
            bt(tasteA * seq[i][0], tasteB + seq[i][1], i)

    for i in range(N):
        bt(seq[i][0], seq[i][1], i)
    print(minDiff[0])
solution()