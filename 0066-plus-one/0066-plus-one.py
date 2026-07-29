class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        op=""
        for i in range(len(digits)):
            op+=str(digits[i])
        num=int(op)+1
        digit=[int(x) for x in str(num)]
        return digit
        