// Last Updated: 5/15/2026, 11:11:07 PM
/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function(newValue){
            if (val===newValue) return true;
            else throw new Error('Not Equal');
        },
        notToBe: function(newValue){
            if (val!==newValue) return true;
            else throw new Error('Equal');
        }
    };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */