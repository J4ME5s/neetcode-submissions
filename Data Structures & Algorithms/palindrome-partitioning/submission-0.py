class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, cur):
            if i == len(s):
                res.append(cur.copy())
                return
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr == substr[::-1]:
                    cur.append(substr)
                    backtrack(j, cur)
                    cur.pop()
        
        backtrack(0, [])
        return res