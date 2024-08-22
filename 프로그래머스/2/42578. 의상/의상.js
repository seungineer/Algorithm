function solution(clothes) {
    var answer = 0;
    const clothes_dict = {};
    clothes.forEach(([value, key]) => {
        clothes_dict[key] = (clothes_dict[key] || 0) + 1;
    });
    const values = Object.values(clothes_dict)
    answer = values.reduce((acc, cur) => {
        console.log(acc)
        return acc*(cur+1)
    }, 1);
    return answer - 1;
}