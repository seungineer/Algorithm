lst = list(map(int, input().split()))

lst_desc = sorted(lst, reverse=True)
lst_asc = sorted(lst, reverse=False)

original = ''.join(map(str,lst))
desc = ''.join(map(str,lst_desc))
asc = ''.join(map(str,lst_asc))

if original == desc:
    print("descending")
elif original == asc:
    print("ascending")
else:
    print("mixed")