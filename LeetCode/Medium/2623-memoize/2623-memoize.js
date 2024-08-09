/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let args_map = new Map();
    
    return function(...args) {
        let args_str = JSON.stringify(args);
        if (args_map.has(args_str)) {
            return args_map.get(args_str);
        } else {
            let res = fn(...args);
            args_map.set(args_str, res);
            return res;
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