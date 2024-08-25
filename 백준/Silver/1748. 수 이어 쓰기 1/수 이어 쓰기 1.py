N = int(input())

# 1~9           9 * 1
# 10 ~ 99       90 * 2
# 100 ~ 999     900 * 3
# 1000 ~ 9999   9000 * 4
N_str = str(N)
length = len(N_str)

default_len = length - 1
answer = 0
for i in range(default_len):
    answer += 9 * (10**i) * (i+1)
if length > 1:
    answer += (N - 10**(length - 1)+1) * length
else:
    answer  += (int(N_str)) * length

print(answer)