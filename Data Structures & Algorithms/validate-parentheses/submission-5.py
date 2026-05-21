class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        
        for i in range(0, len(s), 1):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                if i == len(s) - 1:
                    return False
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if top == "(" and s[i] != ")":
                    return False
                elif top == "{" and s[i] != "}":
                    return False
                elif top == "[" and s[i] != "]":
                    return False
                stack.pop()
        if len(stack) != 0:
            return False
        return True