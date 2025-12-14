class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res=0
        res1=sorted(heights)
        for i in range(len(heights)):
            if heights[i] != res1[i]:
                res+=1
            
        return res

        
        