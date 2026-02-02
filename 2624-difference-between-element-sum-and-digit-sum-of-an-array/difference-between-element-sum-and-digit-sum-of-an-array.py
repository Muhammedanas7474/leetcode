class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        # ele=0
        # digi=0
        # for i in nums:
        #     ele+=i
        # for j in nums:
        #     str_j=str(j)
        #     for k in str_j:
        #         int_k=int(k)
        #         digi+=int_k
        # return ele-digi    



        element_sum=sum(nums)
        digit_sum=sum(int(j) for i in nums for j in str(i))

        return element_sum-digit_sum
        
        