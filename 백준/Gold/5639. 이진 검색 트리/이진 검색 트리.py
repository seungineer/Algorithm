import sys
sys.setrecursionlimit(10**9)

preorder_seq = []
while True:
    try:
        preorder_seq.append(int(input()))
    except:
        break


def postorder(start, end):
    if start > end:
        return
    mid = end + 1
    
    for i in range(start+1, end+1):
        if preorder_seq[i] > preorder_seq[start]:
            mid = i
            break
    postorder(start+1, mid-1)
    postorder(mid, end)
    print(preorder_seq[start])

postorder(0, len(preorder_seq) -1)
