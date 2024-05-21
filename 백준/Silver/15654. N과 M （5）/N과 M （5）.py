n, m = map(int, input().split())
seq = sorted(list(map(int,input().split())))
            
import itertools
nPr = list(itertools.permutations(range(n), m))
for candidate_set in nPr:
    for i in candidate_set:
        print(seq[i], end= ' ')
    print()