class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def backtrack(path, used):
            if len(path) == n:
                self.count += 1
                if self.count == k:
                    self.result = path[:]
                return

            for i in range(1, n + 1):
                if i in used:
                    continue
                path.append(i)
                used.add(i)
                backtrack(path, used)
                path.pop()
                used.remove(i)

        self.count = 0
        self.result = []
        backtrack([], set())
        return ''.join(map(str, self.result))