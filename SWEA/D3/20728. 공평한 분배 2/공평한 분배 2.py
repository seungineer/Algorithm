# N개의 주머니
# 각 주머니에는 사탕 ai개
# k개 선택하여서 아이들에게 나눠 줄 예정
# 가장 많은 것과 적은 것의 사탕 개수 차이 최소화
# 슬라이딩 윈도우 문제

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sack = list(map(int, input().split()))
    sack.sort()
    st = 0
    en = K - 1
    min_diff = sack[en] - sack[st]
    for i in range(N-K+1):
        diff = sack[en] - sack[st]
        min_diff = min(min_diff, diff)
        st += 1
        en += 1
    print(f"#{tc} {min_diff}")


    
