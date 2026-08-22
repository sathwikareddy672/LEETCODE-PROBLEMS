class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s,m=0,1
        for i in str(n):
            s+=int(i)
            m*=int(i)
        return n%(s+m)==0
        