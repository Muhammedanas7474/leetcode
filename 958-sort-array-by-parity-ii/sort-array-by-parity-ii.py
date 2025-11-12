class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [x for x in nums if x % 2 == 0]
        odd = [x for x in nums if x % 2 != 0]
        res = []

        for e, o in zip(even, odd):
            res.append(e)
            res.append(o)

        return res
