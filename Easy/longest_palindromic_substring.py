"""
Given a string s, find the longest palindromic substring in s. You may assume
that the maximum length of s is 1000.
"""

class Solution(object):
	def is_longest(self, s, bottom, top):
		"""
		:type s: str
		:rtype: str
		"""
		n = top - bottom + 1
		if n == 1:
			return s
		mid = n // 2
		low, high = -1, -1
		l, r = mid, mid
		if not n % 2:
			l = mid - 1
		l_substr = self.longestPalindrome(s[:mid])
		r_substr = self.longestPalindrome(s[mid:])
		while l and r < top:
			if s[l] == s[r]:
				low, high = l, r
				l, r = l - 1, r + 1
			else:
				break
		substr = l_substr if len(l_substr) > len(r_substr) else r_substr
		if l != -1 and r != -1 and high - low + 1 > len(substr):
			return s[low:high + 1]
		return substr
		
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if not s:
			return 0
		return self.is_longest(s, 0, len(s) - 1)

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.longestPalindrome("babad")
	if ex_0 != "bab":
		print("Error")
	# Note: "aba" is also a valid answer.
	ex_1 = s.longestPalindrome("cbbd")
	if ex_1 != "bb":
		print("Error")
	ex_2 = s.longestPalindrome("1234432189")
	if ex_2 != "12344321":
		print("Error")
	pass

