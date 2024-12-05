import sys
input = sys.stdin.readline
string1 = input().rstrip()
string2 = input().rstrip()
len_str1 = len(string1)
len_str2 = len(string2)
if len_str1 > len_str2:
    string1, string2 = string2, string1
    len_str1, len_str2 = len_str2, len_str1

common_length = [[0 for _ in range(len_str2)] for _ in range(len_str1)]

answer = 0
for i in range(len_str1):
    for j in range(len_str2):
        if string1[i] == string2[j]:
            if 0 <= i - 1 and 0 <= j - 1:
                common_length[i][j] = common_length[i-1][j-1] + 1
                answer = max(answer, common_length[i][j])
            else:
                common_length[i][j] = 1
print(answer)