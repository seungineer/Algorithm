T = int(input())
for _ in range(T):
    N = int(input()) # 1~N
    answer = []

    def check(eq):
        tot = 0
        prev = ''
        for i in range(len(eq)-1,0,-1):
            if eq[i] not in cand:
                # 숫자인 케이스
                if eq[i-1] == ' ':
                    prev = str(eq[i]) + prev
                else:
                    prev = str(eq[i]) + prev
                    if eq[i-1] == '+':
                        tot += int(prev)
                    else:
                        tot -= int(prev)
                    prev = ''
        prev = str(eq[0]) + prev
        tot += int(prev)
        if tot == 0 : return True
        else: return False

    cand = ['+', '-', ' ']
    def bt(eq, number):
        eq += str(number)
        if len(eq) == (2*N-1):
            if check(eq): answer.append(eq)
            return
        for i in range(3):
            eq += cand[i]
            bt(eq, number + 1)
            eq = eq[:-1]
    bt('', 1)
    answer.sort()
    for ans in answer: print(''.join(map(str, ans)))
    print()