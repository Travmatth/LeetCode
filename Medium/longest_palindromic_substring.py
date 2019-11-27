"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, n, max = 0, len(s), 1
        tbl = [[False for _ in range(n)] for _ in range(n)]
        # all strings of len 1 are palindromes
        for i in range(n):
            tbl[i][i] = True
        # check for substring of len 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                tbl[i][i + 1] = True
                start = i
                max = 2
        # check lengths > 2, k is len of substring
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                # checking for sub-string from i-th to j
                # iff s[i + 1] to s[j - 1] is palindrome
                if tbl[i + 1][j - 1] and s[i] == s[j]:
                    tbl[i][j] = True
                    if k > max:
                        start = i
                        max = k
        return s[start: start + max]

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.longestPalindrome("babad")
    if ex_0 != "bab" and ex_0 != "aba":
        print("ERROR")
    ex_1 = s.longestPalindrome("cbbd")
    if ex_1 != "bb":
        print("ERROR")
    ex_2 = s.longestPalindrome("1234432189")
    if ex_2 != "12344321":
        print("ERROR")
    ex_3 = s.longestPalindrome("9812344321")
    if ex_3 != "12344321":
        print("ERROR")
    ex_4 = s.longestPalindrome("habdba")
    if ex_4 != "abdba":
        print("ERROR")
    pass