class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum=0
        for ch in sentences:
            count=len(ch.split())
            if count>maximum:
                maximum=count
        return maximum
        
        