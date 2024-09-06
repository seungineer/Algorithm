N = int(input())
seq = input()
if N == 1:
    print(int(seq))
    exit()
dp = [[0,0,0] for _ in range((N+1)//2)]
def calcI(i, isBind):
    # 이미 묶여진 것(1) 또는
    # 안 묶여진 것(0) 안 묶을 때 계산 함수
    j = 2 * i
    if seq[j-1] == '+':
        return dp[i-1][isBind] + int(seq[j])
    if seq[j-1] == '-':
        return dp[i-1][isBind] - int(seq[j])
    if seq[j-1] == '*':
        return dp[i-1][isBind] * int(seq[j])
    
def calcINow(i, isMax):
    j = 2 * i
    if seq[j-1] == '+':
        subRes = int(seq[j-2]) + int(seq[j])
    if seq[j-1] == '-':
        subRes = int(seq[j-2]) - int(seq[j])
    if seq[j-1] == '*':
        subRes = int(seq[j-2]) * int(seq[j])
    if isMax == 1:
        if seq[j-3] == '+':
            return max((dp[i-2][0] + subRes),(dp[i-2][1] + subRes),(dp[i-2][2] + subRes))
        if seq[j-3] == '-':
            return max((dp[i-2][0] - subRes),(dp[i-2][1] - subRes),(dp[i-2][2] - subRes))
        if seq[j-3] == '*':
            return max((dp[i-2][0] * subRes),(dp[i-2][1] * subRes),(dp[i-2][2] * subRes))
    else:
        if seq[j-3] == '+':
            return min((dp[i-2][0] + subRes),(dp[i-2][1] + subRes), (dp[i-2][2] + subRes))
        if seq[j-3] == '-':
            return min((dp[i-2][0] - subRes),(dp[i-2][1] - subRes), (dp[i-2][2] - subRes))
        if seq[j-3] == '*':
            return min((dp[i-2][0] * subRes),(dp[i-2][1] * subRes), (dp[i-2][2] * subRes))

dp[0][0] = int(seq[0])
dp[0][1] = int(seq[0])
dp[0][2] = int(seq[0])
dp[1][0] = calcI(1, 0)
dp[1][1] = dp[1][0] #처음에 바로 묶인 것이라 생각
dp[1][2] = dp[1][0] #처음에 바로 묶인 것이라 생각

for i in range(2, (N+1)//2):
    dp[i][0] = calcI(i, 0)
    dp[i][1] = max(calcI(i, 1),calcI(i, 2), calcINow(i, 1))
    dp[i][2] = min(calcI(i, 1),calcI(i, 2), calcINow(i, 2))
print(max(dp[-1][1],dp[-1][2]))

