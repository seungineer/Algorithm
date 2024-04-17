import sys
read = sys.stdin.readline

n = int(read())
card_list = list(map(int, read().split()))
m = int(read())
seq = list(map(int, read().split()))

dict = {}

for k in card_list:
    if k in dict.keys():
        dict[k] += 1
    else:
        dict[k] = 1

for m in seq:
    if m in dict.keys():
        print(dict[m], end=' ')
    else:
        print(0, end= ' ')