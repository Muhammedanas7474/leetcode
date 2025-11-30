class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for i in operations:
            if i == "C":
                res.pop()
            elif i == "D":
                last=res[-1]
                res.append(last*2)
            elif i == "+" :
                last_two_sum=res[-1]+res[-2]
                res.append(last_two_sum)
            else:
                res.append(int(i))
        return sum(res)
