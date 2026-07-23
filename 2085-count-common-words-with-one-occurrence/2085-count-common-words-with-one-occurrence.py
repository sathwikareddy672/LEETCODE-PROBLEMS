class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1,d2={},{}
        count=0
        for ch1 in words1:
            if ch1 in d1:
                d1[ch1]+=1
            else:
                d1[ch1]=1
        for ch2 in words2:
            if ch2 in d2:
                d2[ch2]+=1
            else:
                d2[ch2]=1
        for i in d1:
            if d1[i]==1 and i in d2 and d2[i]==1:
                count+=1
        return count
        