import java.util.*;

class Solution {
    public int[] solution(String s) {
        ArrayList<String> ans = new ArrayList<>();
        HashSet<String> cand = new HashSet<>();
        // 문자열을 분리해서 튜플의 개수가 작은 순으로 오름차순 정렬
        // 각 튜플을 순회하면서 answer에 없는 것은 answer에 추가함
        s = s.replace("{{", "");
        s = s.replace("}}", "");
        s = s.replace("},{", "-");
        String[] sArr = s.split("-");
        ArrayList<String[]> tmp = new ArrayList<>();
        for (int i=0; i<sArr.length; i++) {
            tmp.add(sArr[i].split(","));
        }
        
        tmp.sort((arr1, arr2) -> arr1.length - arr2.length);
        
        for (String[] t: tmp) {
            for (String k: t) {
                if (cand.contains(k)) continue;
                ans.add(k);
                cand.add(k);
            }
        }
        
        int[] answer = new int[ans.size()];
        for (int i=0; i<ans.size(); i++) {
            answer[i] = Integer.parseInt(ans.get(i));
        }
        
        return answer;
    }
}