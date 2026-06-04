class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        realcount = sorted(count, key=lambda x: count[x], reverse=True)

        return realcount[:k]