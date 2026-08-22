class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        r=len(l)
        op=""
        while r>0:
            op+=" "+l[r-1]
            r-=1
        return op[1:]

        