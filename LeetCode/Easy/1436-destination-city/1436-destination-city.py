class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        dict = {}
        for k in paths:
            dict[k[0]] = k[1]
        st = paths[0][0]
        while st in dict.keys():
            st = dict[st]
        return st