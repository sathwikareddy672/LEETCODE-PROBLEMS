class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s,m=0,1
        for j in str(n):
            s+=int(j)
        for i in str(n):
            m*=int(i)
        return n%(s+m)==0
        