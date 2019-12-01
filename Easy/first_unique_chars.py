"""
Given a string, find the first non-repeating character in it and return
it's index. If it doesn't exist, return -1.
Note: You may assume the string contain only lowercase letters. 
"""

class Solution(object):
	def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		freq = {}
		for c in s:
			if c in freq:
				freq[c] += 1
			else:
				freq[c] = 0
		for i, c in enumerate(s):
			if not freq[c]:
				return i
		return -1

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.firstUniqChar("leetcode")
	if ex_0 != 0:
		print("ERROR")
	ex_1 = s.firstUniqChar("loveleetcode")
	if ex_1 != 2:
		print("ERROR")
	pass