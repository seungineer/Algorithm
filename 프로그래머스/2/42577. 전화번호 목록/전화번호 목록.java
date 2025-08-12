import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);

        for (int i=0; i<phone_book.length - 1; i++) {
            String lWord = phone_book[i];
            String rWord = phone_book[i+1];
            int len = Math.min(lWord.length(), rWord.length());
            boolean isDiff = false;
            for (int idx=0; idx<len; idx++) {
                if (lWord.charAt(idx) != rWord.charAt(idx)) {
                    isDiff = true;
                    break;
                }
            }
            if (!isDiff) return false;
        }
        return true;
    }
}