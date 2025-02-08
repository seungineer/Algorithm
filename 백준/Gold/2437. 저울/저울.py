def solution():
    N = int(input())
    seq = list(map(int, input().split()))
    seq.sort()
    if seq[0] != 1:
        print(1)
        return
    targetLength = 1
    for i in range(N):
        el = seq[i]
        if targetLength < el:
            break
        targetLength += el
        
    print(targetLength) 
    return

solution()