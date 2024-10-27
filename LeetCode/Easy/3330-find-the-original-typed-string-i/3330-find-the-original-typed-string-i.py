class Solution:
    def possibleStringCount(self, word: str) -> int:
        word_set = set()
    
        for w in word: word_set.add(w)
        answer = 1
        for w in list(word_set):
            prev_idx = -2
            cnt = 1
            for i in range(len(word)):
                if word[i] == w:
                    if prev_idx == i - 1: cnt += 1
                    else: cnt = 1
                    prev_idx = i
                else:
                    answer += cnt - 1
                    cnt = 1
            if cnt != 1: answer += cnt - 1
                    
    
        # print(answer)
        return answer