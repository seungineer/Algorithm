n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(str,input())))

character_position = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
}
character_priority = {}

for char in lst:
    length = len(char)
    for i in range(length):
        character_position[length-i].append(char[i])
        if char[length-i-1] in character_priority.keys():
            character_priority[char[length-i-1]] += 10**(i)
        else:
            character_priority[char[length-i-1]] = 10**(i)

score = [9,8,7,6,5,4,3,2,1,0]
# cntSet = 0
# character_score = {}
# for i in range(10, 0, -1):
#     while character_position[i]:
#         max_prior = -1
#         for c in character_position[i]:
#             if c in character_score.keys():
#                 character_position[i].remove(c)
#                 continue
#             temp = character_priority[c]
#             if max_prior < temp:
#                 max_prior = temp
#                 max_character = c
#         if max_prior != -1:
#             isSet = True
#             character_position[i].remove(max_character)
#             character_score[max_character] = score[cntSet]
#             cntSet += 1
ans = 0
prior = []
for k in character_priority.values():
    prior.append(k)
prior.sort(reverse=True)
for i in range(len(prior)):
    ans += prior[i] * score[i]
print(ans)
# for c in character_priority:
#     ans += character_score[c] * character_priority[c]
# print(ans)
