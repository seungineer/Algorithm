import itertools

str = input().strip()
l = len(str)
seq = []
for d in range(1, l+1):
    length = l - d
    for start in range(d):
        end = start + length
        seq.append(str[start:end+1])

set_seq = set(seq)
print(len(set_seq))
    