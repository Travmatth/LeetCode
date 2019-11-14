"""
Write a function to find the longest common prefix string
	amongst an array of strings.
If there is no common prefix, return an empty string "".
All given inputs are in lowercase letters a-z.
"""

class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		i = 0
		prefix = ""
		minimum = len(strs[0]) 
		for string in strs[1:]:
			val = len(string)
			if val < minimum:
				minimum = val
		for i in range(minimum):
			potential = strs[0][i]
			for string in strs[1:]:
				if string[i] != potential:
					return prefix
			prefix += potential
		return prefix


if __name__ == "__main__":
	s = Solution()   	
	ex_1 = s.longestCommonPrefix(["flower","flow","flight"])
	if ex_1 != "fl":
		print("fail")
	ex_2 = s.longestCommonPrefix(["dog","racecar","car"])
	if ex_2 != "":
		print("fail")
	pass