def solution():
    N = int(input())
    seq = list(map(int, input().split()))
    ans = -1
    def calMaxPoints(isRightHoneyPot):
        if isRightHoneyPot:
            points = seq[::-1]
        else:
            points = seq
        
        leftBeePoint = 0
        rightBeePoint = sum(points) - points[-1]
        maxPoints = -1
        for leftBeeIdx in range(1, N-1):
            leftBeePoint += points[leftBeeIdx-1]
            rightBeePoint -= points[leftBeeIdx]
            maxPoints = max(maxPoints, leftBeePoint + rightBeePoint)
            rightBeePoint += points[leftBeeIdx]
        return maxPoints
    # 꿀통이 왼쪽에 위치한 경우
    ans = max(ans, calMaxPoints(False))
    # 꿀통이 오른쪽에 위치한 경우
    ans = max(ans, calMaxPoints(True))
    # 꿀통이 각 꿀벌 사이에 위치한 경우
    leftBeePoint = 0
    rightBeePoint = sum(seq) - seq[-1]
    for honeyPotIdx in range(1, N-1):
        leftBeePoint += seq[honeyPotIdx]
        rightBeePoint -= seq[honeyPotIdx-1]
        ans = max(ans, leftBeePoint + rightBeePoint)
    print(ans)

solution()