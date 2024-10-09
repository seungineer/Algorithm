N = int(input())
seq = list(map(int, input().split()))
latest_dict = {}
barrier_num = -1
answer = 0
for i in range(N):
    if seq[i] in latest_dict:
        if barrier_num < latest_dict[seq[i]]:
            temp = (i+1 - latest_dict[seq[i]])
            barrier_num = latest_dict[seq[i]]
        else:
            temp = (i+ 1 - barrier_num)
        answer += temp
        latest_dict[seq[i]] = i+1
    else:
        if barrier_num == -1: temp = i+1
        else: temp = i+1 - barrier_num
        answer += temp
        latest_dict[seq[i]] = i+1
print(answer)