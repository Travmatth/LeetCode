class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        cur, longest = 1, 1
        freq = { s[0]: 0 }
        for i, char in enumerate(s):
            if not i:
                continue
            elif char not in freq or i - cur > freq[char]:
                cur += 1
            else:
                if cur > longest:
                    longest = cur
                cur = i - freq[char]
            freq[char] = i
            if cur > longest:
                longest = cur
        return longest

if __name__ == '__main__':
    s = Solution()
    ex_0 = s.lengthOfLongestSubstring("")
    ex_1 = s.lengthOfLongestSubstring("abcabcbb")
    ex_2 = s.lengthOfLongestSubstring("pwwkew")
    ex_3 = s.lengthOfLongestSubstring("dvdf")
