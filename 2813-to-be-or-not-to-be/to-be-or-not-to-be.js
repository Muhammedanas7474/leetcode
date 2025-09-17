/**
 * @param {any} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function(compare) {
            if (val === compare) {
                return true;
            } else {
                throw new Error("Not Equal");
            }
        },
        notToBe: function(compare) {
            if (val !== compare) {
                return true;
            } else {
                throw new Error("Equal");
            }
        }
    };
};

/**
 * Examples:
 */
console.log(expect(5).toBe(5));      // true
console.log(expect(5).notToBe(10));  // true
// expect(5).toBe(10);               // throws "Not Equal"
// expect(5).notToBe(5);             // throws "Equal"
