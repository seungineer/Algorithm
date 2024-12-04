# 유명인 N명 만나기
# 1 ~ N번 유명인까지 순서대로 만나야 함
# i번 유명인: 인기도 Pi 친화력 Ci
# abs(Pi - X) <= Ci 를 만족해야 1 올라간다

N = int(input())
celebrities = [list(map(int, input().split())) for _ in range(N)]
my_famous = 0
for person in celebrities:
    p, c = person
    if abs(p - my_famous) <= c: my_famous += 1

print(my_famous)