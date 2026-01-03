class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=""
        out=[]
        for i in nums:
            res+=str(i)
        for j in res:
            out.append(int(j))

        return out
        

        