"""
Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.
"""

class Solution(object):
    def recursion(self, lst, string, l, r):
        """
        :type: List[str]
        :type n: int
        :rtype: List[str]
        """
        if not l and not r:
            lst.append(string)
        elif not l and r:
            self.recursion(lst, string + ")", l, r - 1)
        elif l == r:
            self.recursion(lst, string + "(", l - 1, r)
        elif r:
            self.recursion(lst, string + "(", l - 1, r)
            self.recursion(lst, string + ")", l, r - 1)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        lst = []
        self.recursion(lst, "", n, n)
        return lst

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.generateParenthesis(3)
    if set(ex_0) != set(["((()))", "(()())", "(())()", "()(())", "()()()"]):
        print("Error")
    ex_1 = s.generateParenthesis(2)
    if set(ex_1) != set(["(())", "()()"]):
        print("Error")
    ex_1 = s.generateParenthesis(1)
    if set(ex_1) != set(["()"]):
        print("Error")
    ex_2 = s.generateParenthesis(0)
    if set(ex_2) != set([]):
        print("Error")
    pass