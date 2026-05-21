class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        index = 0
        stack = []
        while index <= len(tokens) - 1:
            if tokens[index] == "+":
                    top = stack.pop()
                    bot = stack.pop()
                    stack.append(bot + top)
            elif tokens[index] == "-":
                top = stack.pop()
                bot = stack.pop()
                stack.append(bot - top)
            elif tokens[index] == "*":
                top = stack.pop()
                bot = stack.pop()
                stack.append(bot * top)
            elif tokens[index] == "/":
                top = stack.pop()
                bot = stack.pop()
                stack.append(int(bot / top))
            else:
                stack.append(int(tokens[index]))
            index += 1
        
        return stack.pop()