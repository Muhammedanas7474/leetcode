class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts={}
        ans = -1
        for i in arr:
            if i in counts:
                counts[i] +=1
            else:
                counts[i]=1
        
        for num,count in counts.items():
            if num == count:
                if num > ans :
                    ans = num
        return ans
        
        

        