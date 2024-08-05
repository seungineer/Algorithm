/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let filteredArr = [];
    arr.map((value, index) => {
        if (fn(value, index)) {
            filteredArr.push(value)
        }
    })
    return filteredArr
    
};