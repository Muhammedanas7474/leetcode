# class Solution:
#     def selfDividingNumbers(self, left: int, right: int) -> List[int]:
#         res=[]
#         for i in range(left,right):
#             s=str(i)
#             for ch in s:
#                 if int(ch) == 0:
#                     break
#                 elif i % int(ch) != 0:
#                     break
#                 else:
#                     ch % i == 0
        
        
#         return res

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for i in range(left, right + 1):
            s = str(i)
            self_dividing = True  # assume valid until proven false

            for ch in s:
                digit = int(ch)
                if digit == 0 or i % digit != 0:
                    self_dividing = False
                    break

            if self_dividing:
                res.append(i)

        return res

                
        