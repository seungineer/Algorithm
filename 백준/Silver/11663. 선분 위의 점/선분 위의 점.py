import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
def a_min(a):
    st = 0
    en = n-1
    while (st <= en):
        mid = (st + en)//2
        if a <= seq[mid]:
            en = mid - 1
        else:
            st = mid + 1
    return en + 1

def b_max(b):
    st = 0
    en = n-1
    while (st <= en):
        mid = (st + en)//2
        if b < seq[mid]:
            en = mid - 1
        else:
            st = mid + 1
    return en

for _ in range(m):
    a, b = map(int, input().split())
    print(b_max(b) - a_min(a) + 1)


