class Solution:
    def totalMoney(self, n: int) -> int:
        bank=0
        money=1
        invest=0

        for day in range(1,n+1):
            bank+=money+invest
            invest=invest+1

            if day % 7==0:
                money=money+1
                invest=0
        return bank



            
        