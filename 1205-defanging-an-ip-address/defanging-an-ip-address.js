/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
    res=""
    let add=address.split("")
    for(x of add){
        if(x==="."){
            res +="[.]"
        }else{
            res +=x
        }
    }
    return res
};