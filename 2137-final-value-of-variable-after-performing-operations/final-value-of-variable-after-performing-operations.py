class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in operations :
            if i == "X++":
                x+=1
            elif i =="++X":
                x+=1
            elif i == "--X":
                x-=1
            elif i =="X--":
                x-=1
            else:
                print("This is not valid operator")
        return x