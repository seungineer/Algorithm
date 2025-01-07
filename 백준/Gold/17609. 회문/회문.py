TC = int(input())

def solve(l, r):
    while l <= r:
        if word[l] == word[r]:
            l += 1
            r -= 1
        else:
            if l < r - 1:
                temp = word[:r] + word[r+1:]
                if temp[:] == temp[::-1]:
                    return 1
            if l + 1 < r:
                temp = word[:l] + word[l+1:]
                if temp[:] == temp[::-1]:
                    return 1
            if l + 1 == r:
                return 1
            
            return 2
    return 0    

for _ in range(TC):
    word = input()
    l = 0
    r = len(word) - 1
    print(solve(l, r))