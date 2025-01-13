class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            line_length = 0
            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            line = words[i:j]
            if j == n or len(line) == 1:
                result.append(' '.join(line).ljust(maxWidth))
            else:
                total_spaces = maxWidth - line_length
                spaces = total_spaces // (len(line) - 1)
                extra_spaces = total_spaces % (len(line) - 1)
                for k in range(extra_spaces):
                    line[k] += ' '
                result.append((' ' * spaces).join(line))

            i = j

        return result