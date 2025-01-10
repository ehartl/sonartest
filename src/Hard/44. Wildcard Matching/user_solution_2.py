class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0
        last_match, star = 0, -1

        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                last_match = i
                star = j
                j += 1
            elif star != -1:
                j = star + 1
                i = last_match + 1
                last_match += 1
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
        ##Upvote me If it helps
