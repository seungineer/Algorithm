import sys
import itertools

N = int(sys.stdin.readline())
dogs = list(map(int, sys.stdin.readline().split()))


def count_half(arr):
    line = []
    idx = 0
    count = 0
    for i in arr:
        idx += i
        line.append(idx)
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            if line[i] + 50 == line[j]:
                count += 1
    return count


answer = 0
if max(dogs) > 50:
    print(0)
else:
    cases = list(itertools.permutations(dogs))
    for i in cases:
        line_num = count_half(i)
        answer = max(answer, line_num)

    print(answer)