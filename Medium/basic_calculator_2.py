"""
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers,
+, -, *, / operators and empty spaces . The integer division should
truncate toward zero.
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""

class Solution(object):
    def factor(self, s, i):
        """
        :type s: str
        :rtype: int
        """
        mag, val = 0, 0
        while i < len(s) and s[i] == ' ':
            i += 1
        while i < len(s) and ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
            val = (val * 10) + (ord(s[i]) - ord('0'))
            mag += 1
            i += 1
        return i, val

    def expr(self, s, i):
        """
        :type s: str
        :rtype: int
        """
        j, lhs = self.factor(s, i)
        while j < len(s):
            while j < len(s) and s[j] == ' ':
                j += 1
            if j < len(s) and s[j] == '*':
                j, rhs = self.factor(s, j + 1)
                lhs *= rhs 
            elif j < len(s) and s[j] == '/':
                j, rhs = self.factor(s, j + 1)
                lhs //= rhs 
            else:
                return j, lhs
        return j, lhs
    
    def term(self, s, i):
        i, lhs = self.expr(s, 0)
        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1
            if i < len(s) and s[i] == '+':
                i, rhs = self.expr(s, i + 1)
                lhs += rhs 
            elif i < len(s) and s[i] == '-':
                i, rhs = self.expr(s, i + 1)
                lhs -= rhs 
            else:
                return lhs
        return lhs

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.term(s, 0)

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.calculate("3+2*2")
    if ex_0 != 7:
        print("error")
    ex_1 = s.calculate(" 3/2 ")
    if ex_1 != 1:
        print("error")
    ex_2 = s.calculate(" 3+5 / 2 ")
    if ex_2 != 5:
        print("error")
    ex_3 = s.calculate("1337")
    if ex_3 != 1337:
        print("error")
    ex_4 = s.calculate("1+1+1")
    if ex_4 != 3:
        print("error")
    ex_5 = s.calculate("1   ")
    if ex_5 != 1:
        print("error")
    ex_6 = s.calculate("2*3+4")
    if ex_6 != 10:
        print("error")
    pass