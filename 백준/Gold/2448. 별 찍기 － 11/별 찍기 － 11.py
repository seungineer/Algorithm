n= int(input()) # 3*2**k(3, 6, 12, 24 ...)
temp = n // 3
k = 0
while True:
    temp //= 2
    if temp == 0:
        break
    k += 1 #k 값 구하기

matrix = [[' ' for _ in range(6 * (2**k) - 1)] for _ in range(3 * (2**k))]
# 삼각형 전체 큰 거 그리고
left = 0
right = 6 * (2**k) - 1 - 1
for i in range(1, 6 * (2**k) - 1 + 1):
    for j in range(left, right + 1):
        matrix[-i][j] = '*'
    left += 1
    right -= 1

# k가 값이 줄면서 펀치의 사이즈가 작아지는 방식으로 뚫고
# 1/3, 2/3 지점 left, right 지정

def punch(k, i, j):
    width = 6 * (2**(k-1)) - 1
    l = j - width//2
    r = j + width//2
    while l <= r:
        for k in range(l, r+1):
            matrix[i][k] = ' '
        i += 1
        l += 1
        r -= 1
    return

def draw(k, center_i, center_j):
    if k == 0:
        matrix[int(center_i)][int(center_j)] = ' '
    else:
        punch(k, center_i, center_j)
    k -= 1
    if k < 0:
        return
    
    draw(k, center_i - (3*(2**(k-1))), center_j) # 위
    draw(k, center_i + (3*(2**(k-1))), center_j - (6 * (2**(k-1)))) # 좌
    draw(k, center_i + (3*(2**(k-1))), center_j + (6 * (2**(k-1)))) # 우


draw(k, (3 * (2**k))//2,(6 * (2**k) - 1)//2)

for m in matrix:
    print(''.join(m))


 