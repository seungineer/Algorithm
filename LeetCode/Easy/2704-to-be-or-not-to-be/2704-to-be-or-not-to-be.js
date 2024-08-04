/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    const hidden = val;
    let answer = {};
    
    return {
        toBe: (value) => {
            if (hidden === value){
                return true
            }
            else {
                throw new Error("Not Equal")
            }
        },
        notToBe: (value) => {
            if (hidden === value){
                throw new Error("Equal")
            }
            else {
                return true
            }
        }
        
    }
        
}

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */