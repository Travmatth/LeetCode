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
        index = -1
        count = 0
        needle_hash = 0
        rolling_hash = 0

        if not needle or not haystack:
            return 0 if not needle else -1
        needle_len = len(needle)
        haystack_len = len(haystack)
        if (haystack_len < needle_len):
            return -1
        d = 1 << (needle_len - 1)
        for i in range(needle_len):
            rolling_hash = (rolling_hash << 1) + ord(haystack[i])
            needle_hash = (needle_hash << 1) + ord(needle[i])
        for i in range(haystack_len - needle_len + 1):
            if rolling_hash == needle_hash and needle == haystack[i: i + needle_len]:
				index = i
				break
            if i < haystack_len - needle_len:
                rolling_hash = ((rolling_hash - ord(haystack[i]) * d) << 1) + ord(haystack[i + needle_len])
        return index



if __name__ == "__main__":
    s = Solution()
    ex_0 = s.strStr("hello", "ll")
    ex_1 = s.strStr("aaaaa", "bba")
    ex_2 = s.strStr("foobar", "ar")
    ex_3 = s.strStr("foobar", "foo")
    ex_4 = s.strStr("foobar", "foobarbaz")
    pass