"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(2, n + 1):
            one, two = int(s[i - 1: i]), int(s[i - 2: i])
            if one:
                dp[i] += dp[i - 1]
            if two >= 10 and two <= 26:
                dp[i] += dp[i - 2]
        return dp[n]

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.numDecodings("12")
    if ex_0 != 2:
        print("Error")
    # Explanation: It could be decoded as "AB" (1 2) or "L" (12).
    ex_1 = s.numDecodings("226")
    if ex_1 != 3:
        print("Error")
    # Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
    ex_1 = s.numDecodings("2260")
    if ex_1 != 0:
        print("Error")
    pass