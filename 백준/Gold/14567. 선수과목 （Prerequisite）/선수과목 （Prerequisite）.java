import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static int[] needs;
    static int[] answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        needs = new int[N+1];
        answer = new int[N+1];
        Map<Integer, ArrayList<Integer>> graph = new HashMap<>();
        for (int i=1; i<N; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int temp=0; temp<M; temp++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            needs[b]++;
        }
        int level = 1;
        boolean isStop = false;
        while (!isStop) {
            isStop = true;
            int[] prevNeeds = new int[N+1];
            for (int i=0; i<N+1; i++) prevNeeds[i] = needs[i];

            for (int i=1; i<N+1; i++) {
                if (prevNeeds[i] == 0 && answer[i] == 0) {
                    answer[i] = level;
                    isStop = false;
                    if (graph.get(i) == null) continue;
                    for (int j=0; j<graph.get(i).size(); j++) {
                        int next = (int) graph.get(i).get(j);
                        needs[next]--;
                    }
                }
            }
            level++;
        }
        
        for (int i=1; i<N+1; i++) {
            int cnt = answer[i];
            if (i == N) bw.append(""+cnt);
            else bw.append(cnt+" ");
        }
        bw.flush();
    }
}
