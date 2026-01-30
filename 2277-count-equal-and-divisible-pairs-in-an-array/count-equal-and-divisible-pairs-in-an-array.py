class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    r=i*j
                    if r % k == 0:
                        c+=1 
        return c
            
