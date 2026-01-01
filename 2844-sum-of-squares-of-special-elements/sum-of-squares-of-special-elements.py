class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum=0
        n=len(nums)
        for i,v in enumerate(nums):
            idx=i+1

            if n % idx == 0:
                sum+=v*v
                
        return sum
        