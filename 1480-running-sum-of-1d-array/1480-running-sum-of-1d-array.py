class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[nums[0]]
        for i in range(1, len(nums)):
            op=ans[-1]+nums[i]
            ans.append(op)
        return ans