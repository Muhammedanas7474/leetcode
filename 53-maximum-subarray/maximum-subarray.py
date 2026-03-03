class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n=len(nums)
        # res=nums[0]
        # for i in range(n):
        #     curr=0
        #     for j in range(i,n):
        #         curr+=nums[j]
        #         res=max(curr,res)
        # return res

        maxsub=nums[0]
        currsum=0
        for i in nums:
            if currsum < 0:
                currsum=0
            currsum+=i
            maxsub=max(maxsub,currsum)
        return maxsub