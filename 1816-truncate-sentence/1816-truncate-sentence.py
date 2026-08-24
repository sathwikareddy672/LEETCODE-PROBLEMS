class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s1=s.split(" ")
        op=""
        for i in range(0,k):
            op+=" "+s1[i]
        return op[1:]


        