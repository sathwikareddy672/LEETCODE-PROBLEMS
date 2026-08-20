class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))>1:
            r=num%10
            d=num//10
            op=r+d
            num=op
        return num


           