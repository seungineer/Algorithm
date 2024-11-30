# common_cnt가 같다면, idx1, idx2는 가급적 작아야 됨
# common_cnt가 크다면, idx1, idx2는 업데이트 되어야 함
T = int(input())
words_lst = [input() for _ in range(T)]

words = sorted(words_lst)
words.sort()

max_common_cnt = -1
answer = [1e9,1e9,1e9]
isContinuous = False
candidates = dict()
for i in range(len(words) - 1):
    prefix = ''
    word1 = words[i]
    word2 = words[i+1]
    
    if word1 == word2: continue
    if len(word1) > len(word2): word1, word2 = word2, word1
    
    common_cnt = 0
    for k in range(len(word1)):
        if word1[k] == word2[k]:
            common_cnt += 1
            prefix += word1[k]
        else: break
    
    idx1 = words_lst.index(word1)
    idx2 = words_lst.index(word2)
    if idx1 > idx2:
        word1, word2 = word2, word1
        idx1, idx2 = idx2, idx1

    if common_cnt >= max_common_cnt:
        if prefix in candidates:
            candidates[prefix].add((idx1, word1))
            candidates[prefix].add((idx2, word2))
        else:
            candidates[prefix] = set()
            candidates[prefix].add((idx1, word1))
            candidates[prefix].add((idx2, word2))
    
max_len = -1
max_key = ''
# 길이가 가장 길면서 sort했을 때 0인덱스 값이 가장 큰 Key찾기
for key in candidates.keys():
    lst = sorted(list(candidates[key]))
    if max_len < len(key):
        max_len = len(key)
        min_idx = lst[0][0]
        max_key = key
    elif max_len == len(key):
        if min_idx > lst[0][0]:
            min_idx = lst[0][0]
            max_key = key

ans = sorted(list(candidates[max_key]))
print(ans[0][1])
print(ans[1][1])