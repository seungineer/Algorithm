import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<int[]> arr = new ArrayList<>();
        for (int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            arr.add(new int[]{start, 1});
            arr.add(new int[]{end, -1});
        }
        arr.sort(Comparator.comparing(a -> a[0]));

        int prev = arr.get(0)[0];
        int maxRoom = -1;
        int cntRoom = 0;
        for (int[]room: arr) {
            int time = room[0];
            int point = room[1];
            cntRoom += point;
            if (prev != time) {
                maxRoom = Math.max(maxRoom, cntRoom - point);
                prev = time;
            }
        }
        maxRoom = Math.max(maxRoom, cntRoom);
        System.out.println((maxRoom));
    }
}
