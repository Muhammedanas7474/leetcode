class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_set=set(nums)
        res=[]
        n=len(nums)
        for i in range(1,n+1):
            if i not in new_set:
                res.append(i)

        return res

        