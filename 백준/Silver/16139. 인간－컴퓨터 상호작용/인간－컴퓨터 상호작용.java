import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static char[] word;
    static int q;
    static long[][] cnts;
    public static void main(String[] args) throws IOException {
//        문자 순회하면서 각 자리에 어떤 알파벳이 있는지 체크
//        체크된 배열을 기준으로 누적합 만들기
//        각 알파벳별 누적합
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        word = br.readLine().toCharArray();
        cnts = new long[word.length+1][26];

        for (int i=1; i<word.length+1; i++) {
            int ord = (int)word[i-1] - (int)'a';
            cnts[i][ord]++;
        }
        for (int i=1; i<word.length; i++) {
            for (int j=0; j<26; j++) {
                cnts[i+1][j] += cnts[i][j];
            }
        }
        q = Integer.parseInt(br.readLine());
        StringTokenizer st;
        for (int temp=0; temp<q; temp++) {
            st = new StringTokenizer(br.readLine());
            char alpha = st.nextToken().charAt(0);
            int l = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            l++;
            r++;
            bw.write((cnts[r][(int)alpha-(int)'a'] - cnts[l-1][(int)alpha-(int)'a']) + "\n");
        }
        bw.flush();
        bw.close();
    }
}
