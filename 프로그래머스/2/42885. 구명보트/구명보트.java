import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Integer[] arrPeople = new Integer[people.length];
        for (int i=0; i<arrPeople.length; i++) arrPeople[i] = people[i];
        Arrays.sort(arrPeople, Collections.reverseOrder());
        int l = 0;
        int r = arrPeople.length - 1;
        
        while (l < r) {
            int left = arrPeople[l];
            int right = arrPeople[r];
            if (left + right <= limit) {
                answer++;
                l++;
                r--;
                continue;
            }
            answer++;
            l++;
        }
        if (l == r) {
            answer++;
        }
        
        return answer;
    }
}