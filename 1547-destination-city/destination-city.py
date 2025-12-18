class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        out=set()
        for i in paths:
            out.add(i[0])
        
        for i in paths:
            if i[1] not in out :
                return i[1]
        
            
        
        