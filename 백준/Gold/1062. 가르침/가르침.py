def solution():
    N, K = map(int, input().rstrip().split())
    seq = [input().rstrip() for _ in range(N)]
    
    baseWords = ['anta', 'tica']
    base = 0b0
    for word in baseWords:
        for el in word:
            num = ord(el) - 97
            base = base | (0b1 << num)
    
    def bt(currBit, prev, left):
        if left == 0:
            # words 중 몇 개 가능?
            cnt = 0
            for word in seq:
                isFind = True
                for el in word:
                    num = ord(el) - 97
                    if not currBit & (0b1 << num):
                        isFind = False
                if isFind:
                    cnt += 1
            maxCnt[0] = max(maxCnt[0], cnt)
            return
        for word in range(prev+1, 26):
            if (0b1 << word) & currBit: continue
            currBit = currBit | (0b1 << word)
            bt(currBit, word, left-1)
            currBit = currBit & ~(0b1 << word)
    
    maxCnt = [0]
    K -= 5
    if K == 0:
        cnt = 0
        for word in seq:
            isFind = True
            for el in word:
                num = ord(el) - 97
                if not base & (0b1 << num):
                    isFind = False
            if isFind:
                cnt += 1
        maxCnt[0] = max(maxCnt[0], cnt)
    else:
        for word in range(26):
            if (0b1 << word) & base: continue
            base = base | (0b1 << word)
            bt(base, word, K-1)
            base = base & ~(0b1 << word)
    print(maxCnt[0])
    return
solution()