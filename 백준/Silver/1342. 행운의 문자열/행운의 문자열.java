import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int count = 0;
    static Map<String, Integer> maxCnt = new HashMap<>();
    static Map<String, Integer> usedCnt = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        String[] arr = S.split("");

        for (String ch : arr) {
            maxCnt.put(ch, maxCnt.getOrDefault(ch, 0) + 1);
            usedCnt.put(ch, 0);
        }

        for (String ch : maxCnt.keySet()) {
            usedCnt.put(ch, 1);
            bt(new StringBuilder(ch), S.length(), ch);
            usedCnt.put(ch, 0);
        }

        System.out.println(count);
    }

    public static void bt(StringBuilder word, int n, String lastChar) {
        if (word.length() == n) {
            count++;
            return;
        }

        for (String ch : maxCnt.keySet()) {
            if (!ch.equals(lastChar) && usedCnt.get(ch) < maxCnt.get(ch)) {
                usedCnt.put(ch, usedCnt.get(ch) + 1);
                bt(word.append(ch), n, ch);
                word.deleteCharAt(word.length() - 1);
                usedCnt.put(ch, usedCnt.get(ch) - 1);
            }
        }
    }
}
