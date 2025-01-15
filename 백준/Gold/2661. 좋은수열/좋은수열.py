def solution():
    N = int(input())
    
    def check(number):
        l = len(number)
        for length in range(1, (l // 2) + 1):
            str1 = number[-length:]
            str2 = number[-(length*2):-length]
            if str1 == str2: return False
        return True
    
    def bt(left, number):
        if left == 0:
            print(number)
            isFind[0] = True
            return
        for i in range(1, 4):
            if check(number + str(i)):
                bt(left - 1, number + str(i))
            if isFind[0]: break
            
    isFind = [False]
    bt(N-1, '1')

    return
solution()