from heapq import *

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapify(gifts)

        for i in range(k):
            current = heappop(gifts)
            current = int(abs(current) ** (1/2))

            heappush(gifts, -current)

        return -1 * sum(gifts)
