"""
Given a non-empty string s and a dictionary wordDict
containing a list of non-empty words, determine if s
can be segmented into a space-separated sequence of
one or more dictionary words.
Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
"""

class Solution(object):
    def recurse(self, str, word_set):
        if not str:
            return True
        for i in range(len(str) + 1):
            substring = str[:i]
            if substring in word_set:
                if self.recurse(str[i:], word_set):
                    return True
        return False

    def bottom_up_dp(self, str, word_set):
        n = len(str)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                substring = str[i:j + 1]
                # if substr is word, record and continue
                if substring in word_set:
                    dp[i][j] = True
                # else check if substr is combination of words
                else:
                    for k in range(i + 1, j + 1):
                        if dp[i][k - 1] and dp[k][j]:
                            dp[i][j] = True
        return dp[0][-1]

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        # recursive relation
        # return self.recurse(s, word_set)
        # bottom up dp
        return self.bottom_up_dp(s, word_set)

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.wordBreak("leetcode", ["leet", "code"])
    if ex_0 != True:
        print("Error")
    # Explanation: Return true because "leetcode" can be segmented as "leet code".
    ex_1 = s.wordBreak("applepenapple",["apple", "pen"])
    if ex_1 != True:
        print("Error")
    # Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
    #          Note that you are allowed to reuse a dictionary word.
    ex_2 = s.wordBreak("catsandog",["cats", "dog", "sand", "and", "cat"])
    if ex_2 != False:
        print("Error")
    ex_3 = s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
    if ex_3 != False:
        print("Error")
    ex_4 = s.wordBreak("peanutbutter",["peanut", "butter", "pea", "nut", "but", "butter"])
    if ex_4 != False:
        print("Error")
    pass