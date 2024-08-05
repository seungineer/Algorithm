/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let accum = init;
    nums.map((value) => {
        accum = fn(accum, value)
        
    })
    return accum;
};