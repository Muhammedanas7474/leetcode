class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res=0
        
        for i in accounts:
            temp=0
            for j in i:
                temp+=j
                print(temp)
            
            if temp > res:
                res=temp
        return res
        