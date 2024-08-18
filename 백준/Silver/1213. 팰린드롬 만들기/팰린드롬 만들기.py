input_str = input()
length = len(input_str)
dict = {}
for s in input_str:
    if s in dict.keys():
        dict[s] += 1
    else:
        dict[s] = 1
dict_keys = sorted(dict.keys())
answer = ['' for _ in range(length)]
idx = 0
invalid = False
for alphabet in dict_keys:
    if dict[alphabet] % 2 == 0:
        while dict[alphabet] != 0:
            answer[idx] = alphabet
            answer[-(idx+1)] = alphabet
            dict[alphabet] -= 2
            idx += 1
    else:
        while dict[alphabet] != 1:
            answer[idx] = alphabet
            answer[-(idx+1)] = alphabet
            dict[alphabet] -= 2
            idx += 1

    if dict[alphabet] == 1:
        if answer[length//2] == '':
            dict[alphabet] -= 1
            answer[length//2] = alphabet
        else:
            invalid = True
            break
if invalid:
    print("I'm Sorry Hansoo")
else:
    print(''.join(answer))