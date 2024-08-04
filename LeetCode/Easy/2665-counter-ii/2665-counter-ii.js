/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    const init_val = init;
    let cur_val = init;
    return {
        increment: () => {
            cur_val ++;
            return cur_val
        },
        reset: () => {
            cur_val = init_val;
            return cur_val
        },
        decrement: () => {
            cur_val --;
            return cur_val
        }
    }
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */