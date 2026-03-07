class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        for i in str(num):
            digit=int(i)
            
            if digit == 0:
                continue
            if num % digit == 0 :
                count+=1
                
        return count