import heapq
class Solution:
    def resultsArray(self, queries: list[list[int]], k: int) -> list[int]:
        answer = []
        length_sorted = []
        target_len = float("inf")
        for q in queries:
            if len(answer) < k - 1:
                answer.append(-1)
                dist = abs(q[0]) + abs(q[1])
                heapq.heappush(length_sorted, -dist)
                continue
            dist = abs(q[0]) + abs(q[1])
            # print("start", length_sorted)
            if dist < target_len:
                heapq.heappush(length_sorted, -dist)
                # print("k+1 길이 만큼 돼야 함",length_sorted)
                if target_len != float("inf") and k+1 <= len(length_sorted):
                    heapq.heappop(length_sorted)
                # print(length_sorted)
                target_len = -length_sorted[0]
                answer.append(target_len)
            else:
                answer.append(target_len)
        # print(answer)
        return (answer)