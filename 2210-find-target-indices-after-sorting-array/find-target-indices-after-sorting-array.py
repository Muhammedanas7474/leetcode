class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n=sorted(nums)
        res=[]
        for i in range(len(n)):
            if n[i] == target:
                res.append(i)
        return res
