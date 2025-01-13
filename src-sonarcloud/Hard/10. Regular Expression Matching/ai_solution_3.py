class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        stack = [(0, 0)]
        visited = set()

        while stack:
            i, j = stack.pop()
            if (i, j) in visited:
                continue
            visited.add((i, j))

            if j == len(p):
                if i == len(s):
                    return True
                continue

            first_match = i < len(s) and p[j] in {s[i], '.'}
            if j + 1 < len(p) and p[j + 1] == '*':
                stack.append((i, j + 2))
                if first_match:
                    stack.append((i + 1, j))
            elif first_match:
                stack.append((i + 1, j + 1))

        return False