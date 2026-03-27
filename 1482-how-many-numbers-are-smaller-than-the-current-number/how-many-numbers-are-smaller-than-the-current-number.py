class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            su=0
            for j in range(len(nums)):
                if nums[j] < i:
                    su+=1
            res.append(su)
        return res
                
                    