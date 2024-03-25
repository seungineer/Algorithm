n = int(input())
data = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

max_value = -1e9
min_value = 1e9

def dfs(i, arr):
    global add, sub, mul, div, max_value, min_value
    # 한 노드를 기준으로 다음 노드에 연산자를 활용해 계산함
    ## 계산한 것을 바탕으로 다음 노드를 연산자를 활용해 계산
    ### 마지막 노드까지 계산 완료 후 max, min value 업데이트
    if i == n:
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, arr + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, arr - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, arr * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(arr / data[i]))
            div += 1

dfs(1, data[0])
print(int(max_value))
print(int(min_value))
    