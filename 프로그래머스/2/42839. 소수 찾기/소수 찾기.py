def solution(numbers):
    answer = [0]
    en = int(1e7)
    primes = [1 for _ in range(int(en))]
    for i in range(2, en//2 + 1):
        if primes[i] == 1:
            cand = i + i
            while cand < en:
                primes[cand] = 0
                cand += i
    primes[0] = 0
    primes[1] = 0
    def dfs(prev):
        if len(prev) > 0 and primes[int(prev)]:
            answer[0] += 1
            primes[int(prev)] = 0
        for s in numbers:
            if s == '0' and prev == "":
                continue
            if prev.count(s) < numbers.count(s):
                prev += s
                dfs(prev)
                prev = prev[:-1]
    dfs("")
            
    return answer[0]