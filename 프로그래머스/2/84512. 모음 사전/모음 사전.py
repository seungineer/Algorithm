def bt(target):
    if len(target) == 6: return
    
    dictionary[target] = cnt[0]
    
    for nextVal in range(1, 6):
        if len(target) + 1 != 6:
            cnt[0] += 1
            bt(target + str(nextVal))
    

def solution(word):
    answer = 0
    global cnt, dictionary
    cnt = [0]
    dictionary = dict()
    
    for i in range(1, 6):   
        target = str(i)
        cnt[0] += 1
        bt(target)
        
    trans = ""
    for w in word:
        if w == "A":
            trans += "1"
        if w == "E":
            trans += "2"
        if w == "I":
            trans += "3"
        if w == "O":
            trans += "4"
        if w == "U":
            trans += "5"
    
    return dictionary[trans]