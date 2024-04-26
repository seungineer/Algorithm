n = int(input())
seq = list(input().split())
m = int(input())
candidate = list(input().split())

dict = {}

for k in seq:
    if k in dict.keys():
        dict[k] += 1
    else:
        dict[k] = 1

for l in candidate:
    if l in dict.keys():
        print('1', end= ' ')
    else:
        print('0', end= ' ')