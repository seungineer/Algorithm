import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static ArrayList<Integer> arr = new ArrayList<>();
    static ArrayList<Integer> arrIncrease = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreElements()) {
            arr.add(Integer.parseInt(st.nextToken()));
        }
        for (int i=0; i<arr.size(); i++) {
            if (arrIncrease.isEmpty()) {
                arrIncrease.add(arr.get(i));
                continue;
            }
            // 가장 큰 값(가장 끝 값) 보다 작거나 같은 경우
            if (arrIncrease.get(arrIncrease.size()-1) >= arr.get(i)) {
                // 이분 탐색으로 들어갈 자리 찾기
                int idx = binarySearch(arr.get(i));
                arrIncrease.set(idx, arr.get(i));
            } else {
                arrIncrease.add(arr.get(i));
            }
        }
        System.out.println(arr.size() - arrIncrease.size());
    }
    static Integer binarySearch(int val) {
        int l = 0;
        int r = arrIncrease.size()-1;
        int mid = 0;
        while (l < r) {
            mid = (l+r)/2;
            if (arrIncrease.get(mid) > val) {
                r = mid;
            } else if (arrIncrease.get(mid) == val) {
                return mid;
            } else {
                l = mid + 1;
            }
        }
        return r;
    }
}
