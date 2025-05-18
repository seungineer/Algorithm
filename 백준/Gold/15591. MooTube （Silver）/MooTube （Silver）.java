import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, Q;
    static ArrayList<Integer>[] graph;
    static int[][] costs;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for (int i=0; i< N+1; i++) graph[i] = new ArrayList<>();
        costs = new int[N+1][N+1];
        for (int temp=0; temp<N-1; temp++) {
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int q = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            graph[p].add(q);
            graph[q].add(p);
            costs[p][q] = r;
            costs[q][p] = r;
        }
        for (int temp=0; temp<Q; temp++) {
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            BFS(k, v);
        }
    }
    static void BFS(int k, int start) {
        Deque<Integer> qu = new LinkedList<>();
        Set<Integer> vis = new HashSet<>();
        qu.addLast(start);
        vis.add(start);

        while (!qu.isEmpty()) {
            int node = qu.pollFirst();

            for (int nextNode: graph[node]) {
                if (costs[node][nextNode] < k || vis.contains(nextNode)) continue;
                vis.add(nextNode);
                qu.addLast(nextNode);
            }
        }
        
        System.out.println(vis.size()-1);
    }
}
