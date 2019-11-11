"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

"""

class Solution(object):
	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		idx, i = -1, 0
		len_needle = len(needle)
		len_haystack = len(haystack)

		if not needle:
			return 0
		while idx == -1 and i < len_haystack:
			if haystack[i] == needle[0]:
				tmp = 0
				while tmp < len_needle and i + tmp < len_haystack and haystack[i + tmp] == needle[tmp]:
					tmp += 1
				if tmp == len_needle:
					idx = i
			i += 1
		return idx


if __name__ == "__main__":
	s = Solution()
	ex_0 = s.strStr("hello", "ll")
	ex_1 = s.strStr("aaaaa", "bba")
	ex_2 = s.strStr("foobar", "ar")
	ex_3 = s.strStr("foobar", "foo")
	ex_3 = s.strStr("foobar", "foobarbaz")
	pass