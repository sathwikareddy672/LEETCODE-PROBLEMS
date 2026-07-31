class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value=0
        for ch in operations:
            if ch=="++X" or ch=="X++":    
                value+=1
            elif ch=="--X" or ch=="X--":
                value-=1
        return value    
        