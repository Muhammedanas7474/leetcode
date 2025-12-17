class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum=0
        new={}
        for i in nums:
            if i in new:
                new[i]+=1
            else:
                new[i]=1
        for num,count in new.items():
            if count == 1:
                sum +=num
        return sum
