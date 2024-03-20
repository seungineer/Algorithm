import sys
read = sys.stdin.readline

N = int(input())
A = list(map(int, read().split()))
M = int(input())
seq = list(map(int, read().split()))

A.sort()

def binary_search(arr, target):
    st = 0
    en = len(arr)-1

    while st <= en :
        mid = (st + en)//2 

        if arr[mid] == target : return 1

        if arr[mid] < target : st = mid + 1
        else : en = mid - 1

    return 0
for i in range(len(seq)):
    print(binary_search(A, seq[i]))