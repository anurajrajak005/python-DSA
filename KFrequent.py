# K Frequent Elements
from collections import Counter
from heapq import heappush, heappop
def topKFrequent(nums, k: int) -> list[int]:
    freq = Counter(nums)
    heap = []

    for value, freq in freq.items():
        heappush(heap, (freq, value))
        if len(heap)>k:
            heappop(heap)
    print(heap)
    result = []
    while heap:
        result.append(heappop(heap)[1])
    return result
print(topKFrequent([1,1,1,2,2,3], 2))
