class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res={}
        for i in nums:
            if i in res:
                res[i] += 1     
            else:
                res[i] = 1 
            if res[i] > len(nums)/2:
                return i

        

             

                

        