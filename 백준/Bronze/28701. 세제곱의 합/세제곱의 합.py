N = int(input())
lst = []

for i in range(1, N+1):
    lst.append(i)

line_1st = sum(lst)
line_2nd = sum(lst)**2

line_3rd = 0
for j in lst:
    line_3rd += j**3

print(line_1st)
print(line_2nd)
print(line_3rd)