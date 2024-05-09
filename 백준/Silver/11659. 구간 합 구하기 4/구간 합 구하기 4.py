import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
res_seq = [0 for _ in range(n+1)]

for i in range(n):
    res_seq[i+1] = res_seq[i] + seq[i]

for _ in range(m):
    st, en = map(int, input().split())
    print(res_seq[en]-res_seq[st-1])