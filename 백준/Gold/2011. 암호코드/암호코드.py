import sys
input = sys.stdin.readline
password = list(map(int, input().rstrip()))

N = len(password)
dp = [0 for _ in range(N)]

if password[0] == 0: # 0으로 시작하는 경우 불가능
    print(0)
    exit()
dp[0] = 1

for i in range(1, N):
    if password[i] == 0:
        if password[i-1] == 0:
            print(0)
            exit()
        else:
            if password[i-1] != 1 and password[i-1] != 2:
                continue
            if int(str(password[i-1]) + str(password[i])) <= 26:
               if i < 2:
                   dp[i] += 1
               else:
                   dp[i] = dp[i-2]
            else:
                dp[i] = dp[i-1]
    else:
        dp[i] += dp[i-1]
        if password[i-1] != 1 and password[i-1] != 2:
            continue
        if int(str(password[i-1]) + str(password[i])) <= 26:
            if i < 2:
                dp[i] += 1
            else:
                dp[i] += dp[i-2]
    dp[i] %= 1000000

print(dp[-1])