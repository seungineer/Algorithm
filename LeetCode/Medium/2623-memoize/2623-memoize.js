/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let cache = new Map()
    return function(...args) {
        let key = JSON.stringify(args);
        console.log(key);
        if (cache.has(key)) {
            return cache.get(key);
        } else {
        let answer = fn(...args)
        cache.set(key, answer)
        return answer
        }
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */