class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()

        # for i in range(1,len(nums)):
        #     if nums[i] != nums[i-1]+1:
        #         return nums[i-1]+1
        # return len(nums)

        n = len(nums)
        total_sum = n * (n + 1) // 2
        sum_of_array = sum(nums)
        return total_sum - sum_of_array
        