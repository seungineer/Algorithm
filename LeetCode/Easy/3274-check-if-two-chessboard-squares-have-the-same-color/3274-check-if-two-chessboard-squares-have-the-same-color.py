class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        even = {
            'a': 0,
            'c': 2,
            'e': 4,
            'g': 6,
        }
        color1 = " "
        color2 = " "
        if coordinate1[0] in even.keys():
            if int(coordinate1[1]) % 2 == 1:
                color1 = "B"
            else:
                color1 = "W"
        else:
            if int(coordinate1[1]) % 2 == 1:
                color1 = "W"
            else:
                color1 = "B"
        if coordinate2[0] in even.keys():
            if int(coordinate2[1]) % 2 == 1:
                color2 = "B"
            else:
                color2 = "W"
        else:
            if int(coordinate2[1]) % 2 == 1:
                color2 = "W"
            else:
                color2 = "B"
        if color1 == color2:
            return True
        else:
            return False    