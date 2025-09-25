def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        if " " in phone_book[i]:
            phone_book[i] = num.split().join()
    
    
    for i in range(len(phone_book) - 1):
        answer = True
        f1 = phone_book[i]
        f2 = phone_book[i+1]
        min_l = min(len(f1), len(f2))
        isPass = True
        for j in range(min_l):
            if f1[j] != f2[j]:
                isPass = False
                break
        if isPass:
            return False
                
    return True