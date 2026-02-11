class Solution:
    def secondHighest(self, s: str) -> int:
        new=[]
        lr=-1
        slr=-1
        for i in s:
            if i.isdigit():
                new.append(int(i))
        
        for i in new :
            if i > lr:
                slr=lr
                lr=i
            elif lr > i and i > slr:
                slr=i
        return slr

        
        