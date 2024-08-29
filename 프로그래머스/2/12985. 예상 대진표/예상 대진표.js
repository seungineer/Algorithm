function solution(n,a,b)
{
    var answer = 0;
    if (a > b) {
        a, b = b, a;
    }
    while (true) {
        if (a == b) break;
        answer += 1
        if (a % 2) {
            var a_group = Math.floor(a / 2) + 1
        } else {
            var a_group = Math.floor(a / 2)
        }
        if (b % 2) {
            var b_group = Math.floor(b / 2) + 1
        } else {
            var b_group = Math.floor(b / 2)
        }
        a = a_group
        b = b_group
    }


    return answer;
}