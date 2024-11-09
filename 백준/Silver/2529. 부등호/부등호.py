# 숫자 리스트 만들면서 가야겠다
K = int(input())
seq = list(map(str, input().split()))

min_answer = [1e10]
max_answer = [-1e10]
min_answer_str = ['']
max_answer_str = ['']

def dfs(cand, step):
    if step == K:
        cand_num = int(''.join(map(str, cand)))
        if min_answer[0] > cand_num:
            min_answer[0] = cand_num
            min_answer_str[0] = ''.join(map(str, cand))
        if max_answer[0] < cand_num:
            max_answer[0] = cand_num
            max_answer_str[0] = ''.join(map(str, cand))
        return
    isIn = False
    original_step = step
    for next_number in range(10):
        if not next_number in cand:
            isIn = True
            if seq[step] == '<':
                if cand[-1] < next_number:
                    cand.append(next_number)
                    dfs(cand, original_step + 1)
                    cand.pop()
            else:
                if cand[-1] > next_number:
                    cand.append(next_number)
                    dfs(cand, original_step + 1)
                    cand.pop()
    if not isIn: print(cand)

for k in range(10):
    cand = [k]
    dfs(cand, 0)
    
print(max_answer_str[0])
print(min_answer_str[0])