class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res=0
        for i in details:
            age=i[11:13]
            if int(age) > 60 :
                res +=1
        return res
        