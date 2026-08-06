class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha="abcdefghijklmnopqrstuvwxyz"
        s=set(sentence)
        if len(s)==len(alpha):
            return True
        else:
            return False
        