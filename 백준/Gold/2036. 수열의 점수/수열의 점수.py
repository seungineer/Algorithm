N = int(input())
positives = []
negatives = []
zero_cnt = 0
for _ in range(N):
    number = int(input())
    if number > 0: positives.append(number)
    if number == 0: zero_cnt += 1
    if number < 0: negatives.append(number)

positives.sort(reverse= True)
temp = 0
tot_positive = 0
for i in range(len(positives)):
    if i % 2 == 1:
        mul_cand = temp * positives[i]
        sum_cand = temp + positives[i]
        temp = max(mul_cand, sum_cand)
        tot_positive += temp
        temp = 0
    else:
        temp = positives[i]
tot_positive += temp

negatives.sort()
temp = 0
tot_negative = 0
for i in range(len(negatives)):
    if i % 2 == 1:
        mul_cand = temp * negatives[i]
        sum_cand = temp + negatives[i]
        temp = max(mul_cand, sum_cand)
        tot_negative += temp
        temp = 0
    else:
        temp = negatives[i]

if zero_cnt > 0:
    if temp < 0:
        temp *= 0

tot_negative += temp

print(tot_positive + tot_negative)