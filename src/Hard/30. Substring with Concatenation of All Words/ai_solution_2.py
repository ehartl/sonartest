from typing import List
from itertools import permutations


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        result = []

        for perm in permutations(words):
            target = ''.join(perm)
            start = s.find(target)
            while start != -1:
                result.append(start)
                start = s.find(target, start + 1)

        return result