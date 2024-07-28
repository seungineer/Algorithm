class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def isPrime(num):
            if num < 2:
                return False
            sqrt_num = int(num**0.5)
            vis = [0] * (sqrt_num + 1)
            for i in range(2, sqrt_num + 1):
                if vis[i] == 0:
                    if num % i == 0:
                        return False
                    for j in range(i * i, sqrt_num + 1, i):
                        vis[j] = 1
            return True

        diff = r - l + 1
        cnt = 0
        sqrt_r = int(r**0.5)
        
        for i in range(2, sqrt_r + 1):
            if isPrime(i):
                square = i * i
                if square > r:
                    break
                if square >= l:
                    cnt += 1

        return diff - cnt