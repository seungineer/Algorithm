import sys
read = sys.stdin.readline


ranked_list = []

for _ in range(int(read())):
    n = int(read())
    for _ in range(n):
        doc_rank, interview_rank = map(int, input().split())
        ranked_list.append([doc_rank, interview_rank])

    ranked_list.sort(key=lambda x :(x[0]))
    
    cnt = 0
    for i in range(len(ranked_list)):
        if i == 0:
            target_interview_rank = ranked_list[i][1]
            cnt += 1

        else:
            if target_interview_rank >= ranked_list[i][1]:
                target_interview_rank = ranked_list[i][1]
                cnt += 1
    ranked_list = []
    print(cnt)
