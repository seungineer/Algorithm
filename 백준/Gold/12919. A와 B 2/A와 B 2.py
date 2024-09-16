S = input()
T = input()
# T에서 B를 추가하고, 뒤집어진 상태인지,
# 문자열의 뒤에 A가 추가된 것인지 어떻게 알 수 있음?
# B..B (1)
# B..A (1, 2)
# A..B (X)
# A..A (2)
def go(tT):
    if len(tT) < len(S):
        return
    if tT == S:
        print(1)
        exit()
    literal1 = tT[0]
    literal2 = tT[-1]
    if literal1 == 'B' and literal2 == 'B': #1번 케이스
        nT = tT[:0:-1]
        go(nT)
    elif literal1 == 'B' and literal2 == 'A': # 2번 케이스 =
        nT1 = tT[:0:-1]
        nT2 = tT[:-1]
        go(nT1)
        go(nT2)
    elif literal1 == 'A' and literal2 == 'A': #4번 케이스
        nT2 = tT[:-1]
        go(nT2)
    
go(T)
print(0)