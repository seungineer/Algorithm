from bisect import bisect_right, bisect_left
def solution():
    N = int(input())
    seq = list(map(int, input().split()))
    lis = [seq[0]]
    for i in range(1, N):
        el = seq[i]
        if lis[-1] < el:
            lis.append(el)
        else:
            idx1 = bisect_left(lis, el)
            idx2 = bisect_right(lis, el)
            # 두 인덱스가 같으면 lis 내 el가 존재하지 않음
            if idx1 == idx2:
                lis[idx1] = el

    print(len(lis))
    return

solution()