from bisect import bisect_right, bisect_left
def solution():
    N, S = map(int, input().split())
    seq = list(map(int, input().split()))
    # 절반에 대한 부분 수열의 합 구하기
    partialSeqA = []
    partialSeqB = []
    
    # N이 1일 때, 예외 처리 필요
    if N == 1:
        if seq[0] == S:
            print(1)
        else:
            print(0)
        exit()
    
    cnt = [0]
    def bt(subSum, idx, en, type):
        if subSum == S:
            cnt[0] += 1
        if type == 'A':
            partialSeqA.append(subSum)
        if type == 'B':
            partialSeqB.append(subSum)
        
        for i in range(idx+1, en):
            bt(subSum + seq[i], i, en, type)
    
    for i in range(N//2):
        bt(seq[i], i, N//2, 'A') # [0, N//2)
    for i in range(N//2, N):
        bt(seq[i], i, N, 'B') # [N//2, N)
    SeqA = sorted(partialSeqA)
    SeqB = sorted(partialSeqB)

    for k in SeqA:
        idx1 = bisect_left(SeqB, S-k)
        idx2 = bisect_right(SeqB, S-k)
        if idx1 != idx2:
            cnt[0] += idx2 - idx1
        
    print(cnt[0])
    return

solution()