class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res={}
        
        for i in arr:
            if i in res:
                res[i]=res[i]+1
            else:
                res[i]=1

        seen_counts=[]
        for i in res.values():
            if i in seen_counts:
                return False
            seen_counts.append(i)
        return True
            
            