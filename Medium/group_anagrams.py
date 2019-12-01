"""
Given an array of strings, group anagrams together.
Note:
    All inputs will be in lowercase.
    The order of your output does not matter.
"""

class Solution(object):
	def sort_key(self, v):
		return v[1]

	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		sorted_words = [(i, ''.join(sorted(s))) for i, s in enumerate(strs)]
		sorted_words.sort(key=self.sort_key)
		out, n, i = [], len(strs), 0
		while i < n:
			next = [strs[sorted_words[i][0]]]
			j = 1
			while i + j < n and sorted_words[i][1] == sorted_words[i + j][1]: 
				next.append(strs[sorted_words[i + j][0]])
				j += 1
			out.append(next)
			i += j
		return out

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
	# [["nat","tan"], ["ate","eat","tea"], ["bat"]]
	ex_1 = s.groupAnagrams([""])
	# [[""]]
	ex_2 = s.groupAnagrams([
		"hos","boo","nay","deb","wow","bop","bob","brr",
		"hey","rye","eve","elf","pup","bum","iva","lyx",
		"yap","ugh","hem","rod","aha","nam","gap","yea",
		"doc","pen","job","dis","max","oho","jed","lye",
		"ram","pup","qua","ugh","mir","nap","deb","hog",
		"let","gym","bye","lon","aft","eel","sol","jab"
	])
	# current
	# [
	# ]
	# expected
	# [
	# ["sol"],["wow"],["gap"],["hem"],["yap"],["bum"],["ugh","ugh"],["aha"],
	# ["jab"],["eve"],["bop"],["lyx"],["jed"],["iva"],["rod"],["boo"],["brr"],
	# ["hog"],["nay"],["mir"],["deb","deb"],["aft"],["dis"],["yea"],
	# ["rye"],["hey"],["doc"],["bob"],["eel"],["pen"],["job"],["max"],["oho"],
	# ["lye"],["ram"],["nap"],["elf"],["qua"],["pup","pup"],["let"],["gym"],
	# ["bye"],["lon"]]


	pass

