class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        op=0
        for num in nums:
            if len(str(num))%2==0:
                op+=1
        return op
        