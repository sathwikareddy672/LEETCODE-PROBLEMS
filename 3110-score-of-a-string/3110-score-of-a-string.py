class Solution:
    def scoreOfString(self, s: str) -> int:
        op=0
        for i in range(len(s)-1):
            op+=abs(ord(s[i])-ord(s[i+1]))
        return op
        