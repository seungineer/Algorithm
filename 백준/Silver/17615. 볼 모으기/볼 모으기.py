N = int(input())
seq = list(map(str, input()))
cnt_r = 0
cnt_l = 0
answer_r = 0 # 우측에서 떨어져 있는 B를 오른편으로
answer_l = 0 # 우측에서 떨어져 있는 R를 오른편으로

for s in seq:
    if s == 'B':
        answer_l += cnt_l
        cnt_l = 0
        cnt_r += 1
    if s == 'R':
        answer_r += cnt_r
        cnt_r = 0
        cnt_l += 1
        
print(min(answer_l, answer_r))