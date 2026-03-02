class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_one=0
        max_zero=0
        current_one=0
        current_zero=0

        for i in s:
            if i == "1":
                current_one+=1
                current_zero=0
                max_one=max(current_one,max_one)
            else:
                current_zero+=1
                current_one=0
                max_zero=max(current_zero,max_zero)
        return max_one > max_zero
