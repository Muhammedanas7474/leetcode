class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank={}
        new=sorted(set(arr))
        for i,value in enumerate(new):
            rank[value] = i+1
        res=[]
        for i in arr:
            res.append(rank[i])

        return res
            