class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        new=str(x)
        left=0
        right=len(new)-1

        while left < right :
            if new[left] != new[right]:
                return False
            left+=1
            right-=1
    
        return True
        