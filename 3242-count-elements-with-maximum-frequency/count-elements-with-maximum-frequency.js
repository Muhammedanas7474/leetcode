/**
 * @param {number[]} nums
 * @return {number}
 */
var maxFrequencyElements = function(nums) {
    freq={}
    for(num of nums){
        if(freq[num]===undefined){
            freq[num]=1
            
        }else{
            freq[num]++
        }
    }
    let maxfreq=0
    for(let key in freq ){
       if(freq[key]>maxfreq) {
        maxfreq=freq[key]
       }
    }

    let total=0
    for(let key in freq){
        if(freq[key]===maxfreq){
            total+=freq[key]
        }
    }
    return total
};