class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        op=0
        for ch in stones:
            if ch in jewels:
                op+=1
        return op

        