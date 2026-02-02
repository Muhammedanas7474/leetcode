class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        ele=0
        digi=0
        for i in nums:
            ele+=i

        for j in nums:
            str_j=str(j)
            for k in str_j:
                int_k=int(k)
                digi+=int_k
        return ele-digi    
        
        