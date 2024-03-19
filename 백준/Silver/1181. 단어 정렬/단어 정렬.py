import sys

read = sys.stdin.readline
N = int(read())
data = [read().strip() for _ in range(N)]

#로직
## 중복된 단어는 하나만 남기고 제거
## sorted 함수를 이용해서 정렬할 때, 단어의 길이, 알파벳 순서 우선순위로 정렬한다.

data = list(set(data))
data.sort(key= lambda x :(len(x), x))

for k in data:
    print(k)