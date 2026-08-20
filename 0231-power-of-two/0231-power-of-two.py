class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n%2!=0 and n!=1:
            return False
        x=0
        if n%2==0 or n==1:
            while 2**x<=n :
                if n==2**x:
                    return True
                x+=1
        return False
        
        
        