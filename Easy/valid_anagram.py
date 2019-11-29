"""
Given two strings s and t, write a function to determine
if t is an anagram of s.
Note:
You may assume the string contains only lowercase alphabets.
Follow up:
What if the inputs contain unicode characters? How would you
adapt your solution to such case?
"""

class Solution(object):
	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		chars = [0 for _ in range(26)]
		for char in s:
			pos = ord(char) - ord('a')
			chars[pos] += 1
		for char in t:
			pos = ord(char) - ord('a')
			chars[pos] -= 1
		for freq in chars:
			if freq:
				return False
		return True

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.isAnagram("anagram","nagaram")
	if ex_0 != True:
		print("ERROR")
	ex_1 = s.isAnagram("rat", "car")
	if ex_1 != False:
		print("ERROR")
	pass
