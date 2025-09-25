from math import ceil

def solution(progresses, speeds):
    # 각 작업이 완료되기까지 걸리는 '일수'로 변환
    days = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    answer = []
    cur = days[0]   # 현재 배포 기준일(왼쪽에서 본 최대 완료일)
    cnt = 1         # 현재 배치에 포함된 기능 수

    for d in days[1:]:
        if d <= cur:      # 기준일보다 빨리/같이 끝나면 같은 배치
            cnt += 1
        else:             # 더 오래 걸리면 배치 종료 후 새 배치 시작
            answer.append(cnt)
            cur = d
            cnt = 1

    answer.append(cnt)     # 마지막 배치
    return answer
