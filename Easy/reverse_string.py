"""
Write a function that reverses a string. The input string is given as an array
of characters char[].
Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.
"""

class Solution(object):
	def reverseString(self, s):
		"""
		:type s: List[str]
		:rtype: None Do not return anything, modify s in-place instead.
		"""
		low, high = 0, len(s) - 1
		while low < high:
			s[low], s[high] = s[high], s[low]
			low += 1
			high -= 1

if __name__ == "__main__":
	s = Solution()
	ex_0 = ["h", "e", "l", "l", "o"]
	s.reverseString(ex_0)
	if ex_0 != ["o", "l", "l", "e", "h"]:
		print("ERROR")
	ex_1 = ["H", "a", "n", "n", "a", "h"]
	s.reverseString(ex_1)
	if ex_1 != ["h", "a", "n", "n", "a", "H"]:
		print("ERROR")
	pass