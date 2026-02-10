class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # res=0
        
        # for i in accounts:
        #     temp=0
        #     for j in i:
        #         temp+=j
            
        #     if temp > res:
        #         res=temp
        # return res

        res=0
        for i in accounts:
            current=sum(i)

            if current > res:
                res=current
        return res
        