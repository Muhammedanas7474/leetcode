class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # res=[]
        # n=len(nums)
        # for i in range(1,n+1):
        #     if i not in nums:
        #         res.append(i)

        # return res

        # this is fail in some case becouse of time complexity after this gtp give a method to use 

        res=[]
        new_set=set(nums)
        n=len(nums)

        for i in range(1,n+1):
            if i not in new_set:
                res.append(i)
        return res

        