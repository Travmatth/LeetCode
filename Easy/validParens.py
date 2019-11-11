"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
"""

class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		lookup = { "(": ")", "[": "]", "{": "}" }
		stack = []
		for char in s:
			if char in lookup:
				stack.append(char)
			else:
				if not len(stack):
					return False
				last = stack.pop()
				if lookup[last] == char:
					continue
				return False
		return True if len(stack) == 0 else False

if __name__ == "__main__":
	s = Solution()
	# true
	ex_0 = s.isValid("")
	ex_2 = s.isValid("{}")
	ex_3 = s.isValid("{[]}")
	ex_5 = s.isValid("{[()]}")
	ex_7 = s.isValid("{[()]}()")

	# false
	ex_1 = s.isValid("{")
	ex_4 = s.isValid("{[(]}")
	ex_6 = s.isValid("{[()]}(")
	ex_7 = s.isValid("]")
