class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        count=0
        for ch in arr:
            if ch not in d:
                d[ch]=1
            else:
                d[ch]+=1
        for i in d:
            if d[i]==1:
                count+=1
                if count==k:
                    return i
        return ""