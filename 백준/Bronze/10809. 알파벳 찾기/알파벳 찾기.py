S = input()
lst = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
dic = {}
for i in range(26):
    try:
        if lst[i] in dic.keys():
            print(dic[lst[i]], end= " ")
        else:
            dic[lst[i]] = S.index(lst[i])
            print(dic[lst[i]], end=" ")
    except:
        print(-1, end=" ")