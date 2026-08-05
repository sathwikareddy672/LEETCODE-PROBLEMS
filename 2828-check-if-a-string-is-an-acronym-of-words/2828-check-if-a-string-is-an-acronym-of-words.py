class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        op=""
        for i in words:
            op+=i[0]
        if op==s:
            return True
        return False
        