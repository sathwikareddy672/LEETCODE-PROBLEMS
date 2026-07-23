class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d={}
        op=0
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        for i in d:
            if d[i]==1:
                op+=i
        return op
        