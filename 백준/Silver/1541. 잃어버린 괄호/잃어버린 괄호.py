seq = input().strip()

seq = seq.split('-')
total = []

for k in seq:
    temp = list(map(int,k.split('+')))
    if len(total) >= 1:
        total.append(-sum(temp))
    else:
        total.append(sum(temp))
print(sum(total))