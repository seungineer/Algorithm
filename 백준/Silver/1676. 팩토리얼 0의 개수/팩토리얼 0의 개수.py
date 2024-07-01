import math as m

n = int(input())
# math.factorial(.) 함수를 이용해서 값을 구해줌
n_fac = m.factorial(n)

# 구한 수의 각 자릴수로 리스트를 만들어줌
sep_n = list(str(n_fac))

# 0의 개수 체크
zero_cnt = 0

# 1의 자리부터 -> 리스트에서 제일 뒤쪽부터 -> 리스트의 인덱스 -1부터 -(리스트 길이) 까지 반복하며 체크
for i in range(1, len(sep_n)+1):
  if sep_n[-i] == '0':
    zero_cnt += 1
  else:
    print(zero_cnt)
    break