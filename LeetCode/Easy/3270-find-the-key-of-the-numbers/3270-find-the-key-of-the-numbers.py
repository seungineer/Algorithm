class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        str_num1 = str(num1)
        str_num2 = str(num2)
        str_num3 = str(num3)
        if len(str_num1) != 4:
            str_num1 = '0' * (4-len(str_num1)) + str_num1
        if len(str_num2) != 4:
            str_num2 = '0' * (4-len(str_num2)) + str_num2
        if len(str_num3) != 4:
            str_num3 = '0' * (4-len(str_num3)) + str_num3
        answer = ''
        for digit in range(4):
            answer += min(str_num1[digit], str_num2[digit], str_num3[digit])
        return (int(answer))    