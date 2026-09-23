class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for curr in tokens:
            if curr in "+*-/":
                right = stack.pop()
                left = stack.pop()

                if curr == "+":
                    stack.append(left + right)
                elif curr == "*":
                    stack.append(left * right)
                elif curr == "-":
                    stack.append(left - right)
                else:
                    stack.append(int(left / right))
            else:
                stack.append(int(curr))

        return stack[0]