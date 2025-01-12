from typing import List
from collections import defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = defaultdict(int)

        for word in words:
            word_count[word] += 1

        result = []

        for i in range(word_len):
            left = i
            right = i
            count = 0
            seen = defaultdict(int)

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    seen[word] += 1
                    count += 1

                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == num_words:
                        result.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = right

        return result