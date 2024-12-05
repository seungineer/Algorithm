N, K = map(int, input().split())
words = [input() for _ in range(N)]
selected = set()
for alphabet in 'anta': selected.add(alphabet)
for alphabet in 'tica': selected.add(alphabet)

unicode_start = ord('a')
unicode_end = ord('z')
if K < len(selected):
    print(0)
    exit()
K -= len(selected)
unicodes = list(range(unicode_start, unicode_end + 1))

for el in list(selected):
    unicodes.remove(ord(el))
max_words = [-1]


def count():
    not_cnt = 0
    for word in words:
        for w in word:
            if not w in selected:
                not_cnt += 1
                break
    max_words[0] = max(max_words[0], len(words) - not_cnt)
if K == 0:
    count()
    print(max_words[0])
    exit()

def dfs(index, left):
    if left == 0:
        count()
        return
    
    for k in range(index + 1, len(unicodes)):
        selected.add(chr(unicodes[k]))
        dfs(k, left - 1)
        selected.discard(chr(unicodes[k]))

for i in range(len(unicodes)):
    if chr(unicodes[i]) in selected: continue
    selected.add(chr(unicodes[i]))
    dfs(i, K - 1)
    selected.discard(chr(unicodes[i]))

print(max_words[0])
