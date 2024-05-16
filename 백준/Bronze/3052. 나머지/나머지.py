lst = []
for _ in range(10):
    n = int(input())
    n %= 42
    lst.append(n)
print(len(list(set(lst))))
