class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest=max(candies)
        return [True if candies[i]+extraCandies >=largest else False for i in range(len(candies))]
        
        