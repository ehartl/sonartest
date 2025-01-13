class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
		# Create one iterator per string using zip, it will stop at the shortest string
		# s is a tuple of characters at current position for each string
		# create a set to test unicity
        for s in zip(*strs):
            if len(set(s)) != 1:
                break
            result.append(s[0])
        return "".join(result)
