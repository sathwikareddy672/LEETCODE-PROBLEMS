class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for ch in strs:
            key="".join(sorted(ch))
            if key in d:
                d[key]+=[ch]
            else:
                d[key]=[ch]
        return list(d.values())

        