n = int(input())

#로직
if n < 100:
    cnt = n
elif n <= 1000:
    # 100부터 n까지 반복하면서
    # 반복되는 수 중에서 한수가 있으면 cnt+= 1
    cnt = 99
    for i in range(100, n+1):
        num_1st = i // 100 # 첫째 자리 숫자
        num_2nd = i // 10 % 10 # 둘째 자리 숫자
        num_3rd = i % 100 % 10 # 셋째 자리 숫자
        isArithmeticSeq = num_1st - num_2nd == num_2nd - num_3rd # 한수 판단
        if isArithmeticSeq == True:
            cnt += 1

print(cnt)