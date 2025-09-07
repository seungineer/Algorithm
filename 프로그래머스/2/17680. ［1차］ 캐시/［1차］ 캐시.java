import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        // 큐 내에 도시가 있는 경우 1초 & 기존 것 삭제 후 & 가장 우측에 오도록
        // 큐 내에 도시가 없는 경우 5초 & 가장 우측에 오도록
        // 큐 사이즈가 캐시 사이즈를 넘는 경우 왼쪽부터 빼기
        
        Queue<String> qu = new LinkedList<>();
        for (String city: cities) {
            city = city.toUpperCase();
            
            // qu에 city가 없는 경우
            if (!qu.contains(city)) {
                answer += 5;
                qu.add(city);
            } else {
                // qu에 city가 있는 경우
                answer++;
                qu.remove(city);
                qu.add(city);
            }
            
            if (qu.size() > cacheSize) {
                qu.remove(qu.peek());
            }
        }
        return answer;
    }
}