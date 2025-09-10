/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(n) {
    let pro=1;
    let sum=0
    let num=n.toString().split("").map(Number)

    for(x of num){
        pro =pro*x;
        sum=sum+x
    }

    return pro-sum
    
};