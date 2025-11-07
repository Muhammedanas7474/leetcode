class Solution:
    def addDigits(self, num: int) -> int:
        
    #    while num >= 10:               
    #         current_sum = 0
    #         for i in str(num):         
    #             current_sum += int(i)  
    #         num = current_sum          
    #    return num

        while num >=10:
            num= sum(int(i)for i in str(num))
        return num







        