class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        i = 0
        min_length = 201
        for k in strs:
            min_length = min(min_length, len(k))
        while True:
            if i == min_length:
                return res
            before = ''
            for el in strs:
                print(before, el[i])
                if before == "":
                    before = el[i]
                else:
                    if before == el[i]:
                        before = el[i] # update
                    else:
                        return res

            res += before
            i += 1
        return res