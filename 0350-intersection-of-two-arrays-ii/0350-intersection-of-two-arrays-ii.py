class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        op=[]
        d1,d2={},{}
        for num in nums1:
            if num not in d1:
                d1[num]=1
            else:
                d1[num]+=1
        for nums in nums2:
            if nums not in d2:
                d2[nums]=1
            else:
                d2[nums]+=1
        for i in nums1:
            if i in d2:
                if d1[i]!=0 and d2[i]!=0:
                    op.append(i)
                    d1[i]-=1
                    d2[i]-=1
        return op

            