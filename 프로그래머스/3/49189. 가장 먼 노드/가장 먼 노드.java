import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i=0; i<n; i++) graph.add(new ArrayList<>());
        
        for (int[] e: edge) {
            int a = e[0] - 1;
            int b = e[1] - 1;
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        
        
        int[] vis = new int[n];
        Queue<Integer> qu = new LinkedList<>();
        Integer[] dist = new Integer[n];
        
        vis[0] = 1;
        qu.add(0);
        dist[0] = 0;
        while (!qu.isEmpty()) {
            int curr = qu.poll();
            for (Integer next: graph.get(curr)) {
                if (vis[next] == 1) continue;
                vis[next] = 1;
                dist[next] = dist[curr] + 1;
                qu.add(next);
            }
        }
        int maxDist = -1;
        for (int k: dist) {
            if (k > maxDist) {
                maxDist = k;
                answer = 1;
            } else if (k == maxDist) {
                answer++;
            }
        }
        return answer;
    }
}