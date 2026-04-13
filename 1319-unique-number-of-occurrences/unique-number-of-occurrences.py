class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # res={}
        
        # for i in arr:
        #     if i in res:
        #         res[i]=res[i]+1
        #     else:
        #         res[i]=1

        # seen_counts=[]
        # for i in res.values():
        #     if i in seen_counts:
        #         return False
        #     seen_counts.append(i)
        # return True


        # counts=Counter(arr).values()
        # return len(counts) == len(set(counts))

        counts={}
        for x in arr:
            counts[x] = counts.get(x,0)+1
        freq=counts.values()
        return len(freq) == len(set(freq))
            
            