class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # sum1=0
        # sum2=0
        # res=[]
        # for i in nums1:
        #     if i in nums2:
        #         sum1+=1
        # res.append(sum1)
        # for i in nums2:
        #     if i in nums1:
        #         sum2+=1 
        # res.append(sum2)
        # return res

        set1=set(nums1)
        set2=set(nums2)

        ans1=sum( 1 for i in nums1 if i in set2)
        ans2=sum( 1 for i in nums2 if i in set1)

        return [ans1,ans2]