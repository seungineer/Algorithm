class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        alphabet = [0 for _ in range(26)]
        num_a = ord('a')
        for el in s:
            idx = ord(el) - num_a
            alphabet[idx] += 1
        
        for _ in range(t):
            z_cnt = alphabet[25]
            
            new_alphabet = [0]
            for i in range(len(alphabet) - 1):
                new_alphabet.append(alphabet[i])
            if z_cnt != 0:
                new_alphabet[0] += z_cnt
                new_alphabet[1] += z_cnt
                new_alphabet[0] %= (10**9 + 7)
                new_alphabet[1] %= (10**9 + 7)
            alphabet = new_alphabet.copy()
            # print(alphabet)
        answer = 0
        for el in alphabet:
            answer += el % (10**9 + 7)
        # print(answer % (10**9 + 7))
        return answer % (10**9 + 7)