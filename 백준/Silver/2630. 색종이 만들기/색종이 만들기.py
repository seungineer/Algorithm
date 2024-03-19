import sys

read = sys.stdin.readline
N = int(read())
matrix = [list(map(int, read().split())) for _ in range(N)]

#로직

# 모든 요소가 같은 색인지 판단
# 아니라면 : 가로, 세로 N/2로 쪼개기
## 쪼갠 각각의 사각형에 대해서 위 진행
# 맞다면 : cnt += 1
#        더이상 쪼개지 않음

cnt = [0, 0]

def divided(matrix, bound):        
    divided_matrix1 = []
    divided_matrix2 = []
    divided_matrix3 = []
    divided_matrix4 = []
    for i in range(bound):
        w = matrix[i]
        divided_matrix1.append(w[0:bound])
        divided_matrix2.append(w[bound:len(matrix)])
    for i in range(bound,len(matrix)):
        m = matrix[i]
        divided_matrix3.append(m[0:bound])
        divided_matrix4.append(m[bound:len(matrix)])

    return divided_matrix1, divided_matrix2, divided_matrix3, divided_matrix4

def divide(matrix):
    if len(matrix) ==1:
        if matrix[0][0] == 1:
            cnt[1] +=1 #파란색
        else:
            cnt[0] += 1 #흰색
        return
    flag = True #default
    # 모두 같은 색인지 확인 #
    for i in range(len(matrix)):
        for j in range(len(matrix)-1):
            if matrix[i][j] != matrix[i][j+1]:
              flag = False # 하나라도 다른 색이다.
              break
        if flag == False:
            break
    for j in range(len(matrix)-1):
        for i in range(len(matrix)):
            if matrix[j][i] != matrix[j+1][i]:
              flag = False # 하나라도 다른 색이다.
              break
        if flag == False:
            break
    # 같은색이면 그냥 리턴
    # 다른 색이면 또 쪼개기
    if flag == True:
        if matrix[0][0] == 1:
            cnt[1] +=1 #파란색
        else:
            cnt[0] += 1 #흰색
        return # 더이상 쪼개지 않음
    else:
        # matrix를 N/2로 나눠서
        bound = int(len(matrix) / 2)
        w1, w2, w3, w4 = divided(matrix, bound)
        # 모든 나눠진 애들을 divide 함수에 넣음
        divide(w1)
        divide(w2)
        divide(w3)
        divide(w4)

divide(matrix)
print(cnt[0])
print(cnt[1])