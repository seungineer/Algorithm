N = int(input())

display = []
for cnt in range(1, N+1):
    temp = ' '* (N-cnt)
    temp += '*' * cnt
    display.append(temp)

[print(display[k]) for k in range(N)]
