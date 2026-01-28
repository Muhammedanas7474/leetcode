class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sum1=0
        sum2=0
        res=[]
        for i in nums1:
            if i in nums2:
                sum1+=1
        res.append(sum1)
        for i in nums2:
            if i in nums1:
                sum2+=1
                
        res.append(sum2)
        return res