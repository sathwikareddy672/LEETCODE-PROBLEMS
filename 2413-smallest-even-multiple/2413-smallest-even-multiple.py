class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2!=0:
            op=2*n
        else:
            op=n
        return op 
        