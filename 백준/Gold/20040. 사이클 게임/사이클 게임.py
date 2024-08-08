import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m=map(int,input().split())
parent_lst=[i for i in range(n)]

def find_root(x):
    if x==parent_lst[x]:
        return x
    else:
        parent_lst[x]=find_root(parent_lst[x])
        return find_root(parent_lst[x])

def union(x,y):
    x=find_root(x)
    y=find_root(y)
    if x!=y:
        parent_lst[x]=y

ans=0
for i in range(m):
    a,b=map(int,input().split())
    if ans==0:
        if find_root(a)==find_root(b):
            ans=i+1
    union(a,b)
print(ans)