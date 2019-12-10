"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Note:
Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate
to a result and there won't be any divide by zero operation.
"""

import math

class Solution(object):
    def performOp(self, l, r, op):
        if op == '+':
            return l + r
        elif op == '-':
            return l - r
        elif op == '*':
            return l * r
        elif op == '/':
            return math.trunc(l / float(r))

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        while len(tokens):
            token = tokens.pop(0)
            if token == '+' or token == '-' or token == '*' or token == '/':
                r, l = stack.pop(), stack.pop()
                stack.append(self.performOp(l, r, token))
            else:
                stack.append(int(token))
        return stack.pop()




if __name__ == "__main__":
    s = Solution()
    ex_0 = s.evalRPN(["2", "1", "+", "3", "*"])
    if ex_0 != 9:
        print("Error")
    # Explanation: ((2 + 1) * 3) = 9
    ex_1 = s.evalRPN(["4", "13", "5", "/", "+"])
    if ex_1 != 6:
        print("Error")
    # Explanation: (4 + (13 / 5)) = 6
    ex_2 = s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    if ex_2 != 22:
        print("Error")
    # Explanation: 
    #   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    # = ((10 * (6 / (12 * -11))) + 17) + 5
    # = ((10 * (6 / -132)) + 17) + 5
    # = ((10 * 0) + 17) + 5
    # = (0 + 17) + 5
    # = 17 + 5
    # = 22
    pass