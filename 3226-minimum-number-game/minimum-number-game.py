class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()         
        arr = []
        i = 0

        
        while i < len(nums):
            alice = nums[i]       
            bob = nums[i + 1]     

            
            arr.append(bob)
            arr.append(alice)

            i += 2

        return arr
        

        
        
        



            