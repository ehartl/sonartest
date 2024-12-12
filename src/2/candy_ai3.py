from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Identify peaks and distribute candies
        for i in range(1, n - 1):
            if ratings[i] > ratings[i - 1] and ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i - 1], candies[i + 1]) + 1

        # Traverse left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = max(candies[i], candies[i - 1] + 1)

        # Traverse right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)