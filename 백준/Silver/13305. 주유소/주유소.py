N = int(input())
length = list(map(int, input().split()))
prices = list(map(int, input().split()))
tot = [0 for _ in range(N)]
min_price = float("inf")
for i in range(1, N):
    min_price = min(min_price, prices[i-1])
    tot[i] = tot[i-1] + min_price * length[i-1]
print(tot[-1])
