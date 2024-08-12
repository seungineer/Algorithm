function solution(n, words) {
    var answer = [0, 0];
    const said = new Set();
    let prev_letter = undefined;
    for (let i = 0; i < words.length; i++) {
        const word = words[i]
        if (said.has(word)){
            const num = i % n + 1;
            const cnt = Math.floor(i/n) + 1;
            return [num, cnt]
        }
        if (word[0] == prev_letter || prev_letter === undefined) {
            said.add(word)
            prev_letter = word[word.length-1]
        } else {
            const num = i % n + 1;
            const cnt = Math.floor(i/n) + 1;
            answer = [num, cnt]
            return [num, cnt]
        }
        
    }


    return answer;
}