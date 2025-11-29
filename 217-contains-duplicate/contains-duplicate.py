# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         res=[]
#         for i in nums:
#             if i in res:
#                 return True
#             else:
#                 res.append(i)
#         return False
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
