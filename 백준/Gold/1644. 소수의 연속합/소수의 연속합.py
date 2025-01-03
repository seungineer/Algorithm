def solution(N):
    # N <= 4*(10**6)
    isPrimes = [1 for _ in range(N+1)] # 1이면 소수
    primes = []
    for i in range(2, N+1):
        if not isPrimes[i]: continue
        primes.append(i)
        target = i * 2
        while target <= N:
            isPrimes[target] = 0
            target += i
    M = len(primes)
    if M == 0:
        print(0)
        return
    
    l = 0
    r = 0
    total_sum = primes[0]
    ans = 0
    
    while l <= r and r < M:
        if total_sum < N:
            r += 1
            if r < M: total_sum += primes[r]
        elif total_sum > N:
            total_sum -= primes[l]
            l += 1
            if l > r and l < M:
                r = l
                total_sum = primes[r]
        else:
            ans += 1
            total_sum -= primes[l]
            l += 1
            if l > r and l < M:
                r = l
                total_sum = primes[r]
    print(ans)
    
    
    return
solution(int(input()))