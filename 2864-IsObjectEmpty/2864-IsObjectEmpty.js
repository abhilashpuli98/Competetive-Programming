// Last Updated: 6/22/2026, 12:40:10 AM
/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if(Array.isArray(obj)){
        return obj.length===0;
    }
    else{
        return JSON.stringify(obj)==='{}';
    }
};