import sys
sys.setrecursionlimit(10**5)
def solution():
    S = input()
    ans = [0]

    maxCnt = dict()
    for el in S:
        if el in maxCnt: maxCnt[el] += 1
        else: maxCnt[el] = 1

    def bt(word):
        if len(word) == len(S):
            ans[0] += 1
            return
        for el in maxCnt.keys():
            if word[-1] == el: continue
            if maxCnt[el] > word.count(el):
                if len(word) < len(S):
                    bt(word+el)

    for el in maxCnt.keys():
        bt(el)
    print(ans[0])


solution()