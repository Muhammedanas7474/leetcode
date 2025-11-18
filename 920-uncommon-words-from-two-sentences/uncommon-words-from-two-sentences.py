class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # a=s1.split(" ")
        # b=s2.split(" ")
        # res=[]
        # for i in a:
        #     print(i,a.count(i))
        #     if a.count(i) == 1 and i not in b:
        #         res.append(i)
        # for j in b:
        #     if b.count(j) == 1 and  j not in a:
        #         res.append(j)
        # return res

        words=(s1 + " "+ s2).split()
        res=[]
        for w in words:
            if words.count(w) == 1 :
                res.append(w)
        return res

        