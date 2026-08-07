class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p,s=1,0
        for i in range(len(str(n))):
            r=n%10
            p*=r
            s+=r
            n=n//10

        return p-s
        