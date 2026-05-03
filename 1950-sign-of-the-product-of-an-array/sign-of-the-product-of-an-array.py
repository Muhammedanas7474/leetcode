class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative_count = 0
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                negative_count+=1
        
        return -1 if negative_count % 2 != 0 else 1