class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1,nums2,ans=[],[],[]
        for i in range(len(nums)):
            if i<n:
                nums1.append(nums[i])
            else:
                nums2.append(nums[i])
        for i in range(n):
            ans.append(nums1[i])
            ans.append(nums2[i])
        return ans


        

        