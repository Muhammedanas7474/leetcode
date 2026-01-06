class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res=0
        for i in sentences:
            a=i.split()
            if res < len(a):
                res=len(a)
        return res
                
            

