class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = min(len(ch) for ch in strs)
        op=""
        for i in range(0,r):
            for word in strs:
                if word[i]!=strs[0][i]:
                    return op
            op +=strs[0][i]
        return op

        