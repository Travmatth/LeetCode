"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
"""

class Solution(object):
    def permute_palindrome(self, s, out, cur):
        if not s:
            out.append(cur)
        elif len(s) == 1:
            cur.append(s)
            out.append(cur)
        else:
            for i in range(1, len(s) + 1):
                substring = s[:i]
                if substring == substring[::-1]:
                    decomposition = [c for c in cur]
                    decomposition.append((substring))
                    self.permute_palindrome(s[i:], out, decomposition)

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        out = []
        self.permute_palindrome(s, out, [])
        return out

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.partition("aab")
    if ex_0 != [["aa","b"], ["a","a","b"]]:
        print("ERROR")
    ex_1 = s.partition("banana")
    if ex_1 != [["b", "anana"], ["b", "ana", "n", "a"], ["b", "a", "n", "ana"], ["b", "a", "n", "a", "n", "a"]]:
        print("ERROR")
    pass