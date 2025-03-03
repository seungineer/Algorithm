def solution():
    N, K = map(int, input().split())
    seq = list(map(int, input().split()))
    diff = [seq[i] - seq[i-1] for i in range(1, N)]
    diff.sort(reverse=True)
    print(sum(diff[K-1:]))

solution()