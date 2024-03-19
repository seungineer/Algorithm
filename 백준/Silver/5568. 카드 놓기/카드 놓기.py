import sys

read = sys.stdin.readline
N = int(read())
k = int(read())
data = [int(read()) for _ in range(N)]

#로직
candidate = []

results = set()

def f(seq, candidate, k):
    # k = 0이 될 때까지 반복했으면 숫자 조합 리턴(기저 조건)
    if k == 0:
        
        str_result = ''.join(map(str, candidate))
        results.add(str_result)
        return
    
    #숫자 리스트 중에서 임의의 숫자에 대해 선택
    for i in range(len(seq)):
        if seq[i] == None:
            continue
        next_candidate = candidate + [seq[i]] # candidate 리스트에 할당
        temp = seq[i]
        seq[i] = None
        
        f(seq, next_candidate, k-1)
        seq[i] = temp
    
f(data,candidate,k)
print(len(results))