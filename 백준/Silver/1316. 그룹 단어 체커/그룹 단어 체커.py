n = int(input())
cnt = 0

for _ in range(n):
    flag = True
    word = input().strip()
    word_length = len(word)
    dic = {}
    for i in range(word_length):
        if not word[i] in dic.keys():
            dic[word[i]] = 1
        else:
            if word[i-1] != word[i]:
                dic[word[i]] += 1
                flag = False
        if flag == False:
            break
    if flag == True:
        cnt += 1

print(cnt)