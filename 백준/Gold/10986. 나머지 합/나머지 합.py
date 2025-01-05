def solution():
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))
    # 모듈러 prefix sum
    # prefix sum에서 나머지 후보 개수 세기
    # 0 개수 + 시그마(나머지 후보)C2
    modulo_prefix_sum = [0 for _ in range(N)]
    candidate_cnt = [0 for _ in range(M)]
    modulo_prefix_sum[0] = seq[0] % M
    candidate_cnt[modulo_prefix_sum[0]] += 1
    for i in range(1, N):
        modulo_prefix_sum[i] = (modulo_prefix_sum[i-1] + seq[i] % M) % M
        candidate_cnt[modulo_prefix_sum[i]] += 1
    ans = candidate_cnt[0]
    for i in range(M):
        n = candidate_cnt[i]
        ans += n * (n-1) // 2
    print(ans)
    return

solution()