N = int(input())
#로직

# 함수 : N x N 형태의 사각형에서 중앙(N/3, N/3 지점들)을 뚫어내는 함수
#   뚫어 내야하는 부분의 위치가 계속 바뀌니까 파라미터로 지정
#   n = 1이 되면 return
length = N

plate = []
str = ['*'] * length
cnt = [0]
for i in range(length):
    plate.append(str.copy()) # shallow copy 사용하여 str 변수 내 리스트 한 번에 변경되는 부분 방지

def punch(x, y, length, plate):
    cnt[0] += 1
    if length == 1:
        return
    length //= 3

    # print(f"{cnt}: {x}, {y}")
    # x, y 시작 지점 할당
    # 할당된 곳에서 punch 실행
    for i in range(x, x+length):
        for j in range(y,y+length):
            plate[i][j] = ' ' # 펀치 완료
    x1 = x - length*2//3
    x2 = x + length//3
    x3 = x + length * 4 // 3
    y1 = y - length*2 //3
    y2 = y + length//3
    y3 = y + length*4//3
    # print(f"{x1}, {y1}")
    # print(f"{x2}, {y2}")
    # print(f"{x3}, {y3}")
    

    punch(x1, y1, length, plate)
    punch(x2, y1, length, plate)
    punch(x3, y1, length, plate)
    punch(x1, y2, length, plate)
    punch(x3, y2, length, plate)
    punch(x1, y3, length, plate)
    punch(x2, y3, length, plate)
    punch(x3, y3, length, plate)


x = length//3
y = length//3 # 초기 시작 위치 지정(가운데 펀치 뚫리게)

punch(x, y, length, plate)


formatted_latest_matrix = "\n".join(["".join(row) for row in plate])
print(formatted_latest_matrix)