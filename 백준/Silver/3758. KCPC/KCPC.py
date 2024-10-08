import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    n, k, t, m = map(int, input().split())
    matrix = [[0 for _ in range(k+1)] for _ in range(n)] #팀(행)은 인덱스 고려 필요, 문제번호는 인덱스 고려 필요 X
    sum_lst = [0 for _ in range(n)]
    cnt_lst = [0 for _ in range(n)]
    log_qu = []
    for _ in range(m):
        i, j, s = map(int, input().split())
        cnt_lst[i-1] += 1
        if i in log_qu: log_qu.remove(i)
        log_qu.append(i)
        if matrix[i-1][j] < s:
            sum_lst[i-1] -= matrix[i-1][j]
            matrix[i-1][j] = s
            sum_lst[i-1] += s

    rank = 1
    for i in range(n):
        if i == t-1: continue
        if sum_lst[i] > sum_lst[t-1]:
            rank += 1
        elif sum_lst[i] == sum_lst[t-1]:
            if cnt_lst[i] < cnt_lst[t-1]:
                rank += 1
            elif cnt_lst[i] == cnt_lst[t-1]:
                if log_qu.index(i+1) < log_qu.index(t):
                    rank += 1
    print(rank)