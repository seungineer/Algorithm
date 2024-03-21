x, y = map(int, input().split())

# 1월 1일이 월요일이므로
# N * 7 사각형을 생각하자
##
### 그러면 x월 y일이 1월 1일로부터 얼마나 떨어져 있는지 알면 쉽게 계산 가능
lst1 = [1, 3, 5, 7, 8, 10, 12] #31일까지

tot = 0

for i in range(1, x): #x월 직전까지 tot 일 수 구하기
    if i in lst1:
        tot += 31
    elif i == 2:
        tot += 28
    else:
        tot += 30

sum = tot + y

result = sum % 7

if result == 0:
    print('SUN')
elif result == 1:
    print('MON')
elif result == 2:
    print('TUE')
elif result == 3:
    print('WED')
elif result == 4:
    print('THU')
elif result == 5:
    print('FRI')
else:
    print('SAT')


