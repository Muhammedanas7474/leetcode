/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let n=nums.length
    let res=0
    for(i=0;i<=n;i++){
        if(!nums.includes(i)){
            res=i
        }
    }
    return res
    
};