/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let i = 0;
    var dict = {};
    let cnt = 0;
    let max_cnt = 0;
    while (i != s.length){
        if (s[i] in dict){
            i = i - cnt + 1;
            max_cnt = Math.max(max_cnt, cnt);
            dict = {};
            cnt = 0;
        }
        else{
            dict[s[i]] = 1;
            cnt += 1;
            i += 1;
            if (i == s.length){
                max_cnt = Math.max(max_cnt, cnt);
                break;
            }
        }
    }
    return max_cnt
};