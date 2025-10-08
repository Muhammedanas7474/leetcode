class Solution:
    def reverseWords(self, s: str) -> str:
        r=list(s.split(" "))
        res=[]
        for i in r:
            rev=i[::-1]
            res.append(rev)
        return " ".join(res)
        