import sys
input = sys.stdin.readline

N, M = map(int, input().split( ))

picto = {}

for i in range(N):
    pokemon = input().strip()
    picto.update({pokemon:str(i+1)})
    picto.update({str(i+1):pokemon})

for _ in range(M):
    print(picto[str(input().strip())])