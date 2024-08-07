/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    var answer = args.length;
    return answer;
    
};

/**
 * argumentsLength(1, 2, 3); // 3
 */