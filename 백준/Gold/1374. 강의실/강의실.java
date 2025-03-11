import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(bf.readLine());
        List<int[]> lectures = new ArrayList<>();

        for (int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int n = Integer.parseInt(st.nextToken());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            lectures.add(new int[]{start, 1});
            lectures.add(new int[]{end, -1});
        }

        lectures.sort(Comparator.comparing(a -> a[0]));
        int maxRoom = -1;
        int currentRoom = 0;
        int prevLecture = lectures.get(0)[0];
        for (int[] lecture: lectures) {
            currentRoom += lecture[1];
            if (prevLecture != lecture[0]) {
                maxRoom = Math.max(maxRoom, currentRoom - lecture[1]);
                prevLecture = lecture[0];
            }
        }
        maxRoom = Math.max(maxRoom, currentRoom);
        bw.write(maxRoom +"\n");

        bw.flush();

    }
}
