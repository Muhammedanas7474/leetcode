class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low = min(nums)
        high = max(nums)

        s = set(nums)
        missing = []

        for x in range(low, high + 1):
            if x not in s:
                missing.append(x)

        return missing
        