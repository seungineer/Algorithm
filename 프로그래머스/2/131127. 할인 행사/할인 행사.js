function solution(want, number, discount) {
    let answer = 0;
    const n = want.length;
    const m = discount.length;

    const wants = {};
    for (let i = 0; i < n; i++) {
        wants[want[i]] = number[i];
    }

    const sales = {};
    for (let i = 0; i < 10; i++) {
        sales[discount[i]] = (sales[discount[i]] || 0) + 1;
    }

    const isPossible = () => {
        for (let name of want) {
            if (!sales[name] || sales[name] < wants[name]) {
                return false;
            }
        }
        return true;
    };

    if (isPossible()) answer++;

    for (let j = 10; j < m; j++) {
        sales[discount[j]] = (sales[discount[j]] || 0) + 1;
        sales[discount[j-10]]--;

        if (sales[discount[j-10]] === 0) {
            delete sales[discount[j-10]];
        }

        if (isPossible()) answer++;
    }

    return answer;
}