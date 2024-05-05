n = int(input())

end = 6666666
start = 665
output = 0
while(start != end):
    cnt = str(start).count('666')
    if cnt >= 1:
        output += 1
    if output == n:
        print(start)
        break
    start += 1