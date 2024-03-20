n, m = map(int, input().split())

def reverseNumber(n):    
    temp1 = str(n%10)
    temp2 = str(n%100 //10)
    temp3 = str(n//100)
    reverse_num = int(temp1 + temp2 + temp3)
    return reverse_num

reversed_n = reverseNumber(n)
reversed_m = reverseNumber(m)

if reversed_n > reversed_m:
    print(reversed_n)
else:
    print(reversed_m)
