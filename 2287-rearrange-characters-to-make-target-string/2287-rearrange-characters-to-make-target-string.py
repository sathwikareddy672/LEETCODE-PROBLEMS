class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ds,dt,op={},{},0
        smallest = float('inf')
        for ch in s:
            if ch in ds:
                ds[ch]+=1
            else:
                ds[ch]=1
        for ch in target:
            if ch in dt:
                dt[ch]+=1
            else:
                dt[ch]=1
        for i in dt:
            if i not in ds:
                return 0
            else:
                op=ds[i] // dt[i]
                smallest=min(op,smallest)
        return smallest
