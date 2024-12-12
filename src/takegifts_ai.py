
import math

def remaining_gifts(gifts, k):
    for _ in range(k):
        max_index = gifts.index(max(gifts))
        gifts[max_index] = math.isqrt(gifts[max_index])
    return sum(gifts)

# Example usage
print(remaining_gifts([25, 64, 9, 4, 100], 4))  # Output: 29
print(remaining_gifts([1, 1, 1, 1], 4))  # Output: 4