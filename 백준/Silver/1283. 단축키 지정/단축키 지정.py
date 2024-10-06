# 공백 기준으로 자르고,
# 자른 첫 째 단어 중 앞 단을 넣고
## 넣을 수 있으면 해당 인덱스 구하기 (청크 개수 - 1) + 청크 단어 합
## 여기서 찾지 못할 경우
# 단어를 전체 순회하며 가능한 알파벳 찾기
## 여기서 공백과 대소문자에 유의해서 구하고,
## 인덱스를 뽑아낼 수 있음
N= int(input())
shortcut_set = set()
for _ in range(N):
    name = input()
    name_chunk = name.split(" ")
    cnt = 0
    isFind = False
    for c in name_chunk:
        if not str.lower(c[0]) in shortcut_set:
            shortcut_set.add(str.lower(c[0]))
            isFind = True
            break
        cnt += (len(c) + 1)
    # cnt 인덱스가 단축키 인덱스가 됨
    if isFind:
        name_str1 = name[:cnt]
        name_str2 = name[cnt]
        name_str3 = name[cnt + 1:]
        res_str = name_str1 + '[' + name_str2 + ']' + name_str3
        print(res_str)
        continue
    # name chunk 맨 앞에서 단축키 지정하지 못한 경우에
    isFind = False
    for i in range(len(name)):
        if name[i] == " ": continue
        if str.lower(name[i]) in shortcut_set: continue
        else:
            shortcut_set.add(str.lower(name[i]))
            isFind = True
            cnt = i
            break
    if isFind:
        name_str1 = name[:cnt]
        name_str2 = name[cnt]
        name_str3 = name[cnt + 1:]
        res_str = name_str1 + '[' + name_str2 + ']' + name_str3
        print(res_str)
        continue
    print(name)