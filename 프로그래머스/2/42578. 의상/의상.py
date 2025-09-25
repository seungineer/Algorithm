from collections import defaultdict
def solution(clothes):
    boxes = defaultdict(set)
    for name, types in clothes:
        boxes[types].add(name)
    answer = 1
    for k in boxes.keys():
        answer *= (len(boxes[k]) + 1)
        
    return answer - 1