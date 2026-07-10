import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        checker = Counter(nums)
        heap = []
        for key,count in checker.items():
            heapq.heappush(heap,(count,key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [h[1] for h in heap]
            
        