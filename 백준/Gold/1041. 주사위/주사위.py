# 내부에 포함되는 면은 주사위 숫자 중 가작 작은 값
# 몸통 모셔리 4개
# 윗 뚜껑 모서리 4개

# (0, 5), (1, 4), (2, 3)
# 두 면이 보이는 곳
# 세 면이 보이는 곳
# 한 면이 보이는 곳
N = int(input())
seq = list(map(int, input().split()))
if N == 1:
    min_num = max(seq)
    print(sum(seq) - min_num)
    exit()

for i in range(len(seq)):
    seq[i] = [seq[i], i]

opposite_set = set()
opposite_set.add((0, 5))
opposite_set.add((1, 4))
opposite_set.add((2, 3))

def hasOpposite(lst):
    new_set = set()
    for i in range(len(lst) - 1):
        for j in range(i+1, len(lst)):
            new_set.add((lst[i][1], lst[j][1]))
    sum_set = opposite_set.union(new_set)
    
    if len(sum_set) == len(new_set) + len(opposite_set): return False
    else: return True

def cal_3_surface(seq):
    def dfs(index, lst):
        if len(lst) == 3:
            if not hasOpposite(lst):
                tot = 0
                for el in lst: tot += el[0]
                max_3_surface[0] = min(max_3_surface[0], tot)
            return
        for k in range(index + 1, 6):
            lst.append(seq[k])
            dfs(k, [el for el in lst])
            lst.pop()

    for i in range(5):
        dfs(i, [seq[i]])

def cal_2_surface(seq):
    def dfs(index, lst):
        if len(lst) == 2:
            if not hasOpposite(lst):
                tot = 0
                for el in lst: tot += el[0]
                max_2_surface[0] = min(max_2_surface[0], tot)
            return
        for k in range(index + 1, 6):
            lst.append(seq[k])
            dfs(k, [el for el in lst])
            lst.pop()

    for i in range(5):
        dfs(i, [seq[i]])

max_3_surface = [1e9]
cal_3_surface(seq)
max_2_surface = [1e9]
cal_2_surface(seq)
max_1_surface = [min(seq)[0]]

cnt_3 = 4
cnt_2 = (N-1) * 4 + (N-2) * 4
cnt_1 = (N-2) * (N-1) * 4 + (N - 2) * (N - 2)
print(cnt_3 * max_3_surface[0] + cnt_2 * max_2_surface[0] + cnt_1 * max_1_surface[0])
