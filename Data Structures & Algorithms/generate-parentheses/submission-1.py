class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(left, right, cur):
            if left == right == n:
                res.append("".join(cur.copy()))
                return
            
            if left < n:
                cur.append("(")
                backtrack(left + 1, right, cur)
                cur.pop()
            if left > right:
                cur.append(")")
                backtrack(left, right + 1, cur)
                cur.pop()
            
        backtrack(0, 0, [])
        return res
            