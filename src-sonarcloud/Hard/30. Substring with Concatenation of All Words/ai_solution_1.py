from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = {}

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        result = []

        for i in range(len(s) - total_len + 1):
            seen = {}
            for j in range(num_words):
                word = s[i + j * word_len:i + (j + 1) * word_len]
                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    if seen[word] > word_count[word]:
                        break
                else:
                    break
            if seen == word_count:
                result.append(i)

        return result