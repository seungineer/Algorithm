str1 = list(input().strip())
str2 = list(input().strip())

lcs = [[0] * (len(str2)+1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            lcs[i][j]= lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

result = []
i, j = len(str1), len(str2)
while True:
    if str1[i-1] == str2[j-1]:
        result.append(str1[i-1])
        i -= 1
        j -= 1
    else:
        if lcs[i][j] == lcs[i-1][j]:
            i -= 1
        else:
            j-= 1

    if i == 0 or j == 0:
        break
result = ''.join(result[::-1])

print(lcs[len(str1)][len(str2)])
if lcs[len(str1)][len(str2)] != 0:
    print(result)
    