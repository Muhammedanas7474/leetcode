class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a=s1.split(" ")
        b=s2.split(" ")
        res=[]
        for i in a:
            if a.count(i) == 1 and i not in b:
                res.append(i)
        for j in b:
            if b.count(j) == 1 and  j not in a:
                res.append(j)
        return res

        