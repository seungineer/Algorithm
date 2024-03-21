import sys
read = sys.stdin.readline

n = int(input())

def push(stk, x):
    stk.append(x)

def pop(stk):
    if len(stk)==0:
        print(-1)
    else:
        print(stk[-1])
        stk.pop()

def size(stk):
    print(len(stk))

def empty(stk):
    if len(stk) == 0:
        print(1)
    else:
        print(0)

def top(stk):
    if len(stk) == 0:
        print(-1)
    else:
        print(stk[-1])

stk = []
while n > 0:
    data = list(read().split(" "))
    if len(data) == 2:
        push(stk, int(data[1]))
    else:
        if data[0] == 'pop\n':
            pop(stk)
        elif data[0] =='size\n':
            size(stk)
        elif data[0] =='empty\n':
            empty(stk)
        elif data[0] =='top\n':
            top(stk)
    n -= 1