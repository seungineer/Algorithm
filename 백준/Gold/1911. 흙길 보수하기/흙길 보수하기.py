N, L = map(int, input().split())
pools = [list(map(int, input().split())) for _ in range(N)]
pools.sort()

bar_st = 0
answer = 0
for i in range(N):
    st, en = pools[i]
    if bar_st < st: bar_st = st

    cover_len = en - bar_st
    answer += cover_len // L + 1
    if cover_len % L == 0:
        bar_st += ((cover_len // L) * L - 1)
        answer -= 1
        continue
    bar_st += ((cover_len // L + 1) * L - 1) + 1
print(answer)


