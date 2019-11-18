"""
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty
string as valid palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low, high = 0, len(s) - 1
        l, r = None, None
        while True:
            if low >= high:
                return True
            elif s[low] and not s[low].isalnum():
                low += 1
                continue
            elif high >= 0 and not s[high].isalnum():
                high -= 1
                continue
            l, r = s[low], s[high]
            if l == r:
                low += 1
                high -= 1
                continue
            elif l.isalpha() != r.isalpha():
                return False
            elif l.lower() == r.lower():
                low += 1
                high -= 1
                continue
            return False
            
if __name__ == "__main__":
    s = Solution()
    ex_0 = s.isPalindrome("A man, a plan, a canal: Panama")
    if ex_0 != True:
        print("ERROR")
    ex_1 = s.isPalindrome("race a car")
    if ex_1 != False:
        print("ERROR")
    ex_2 = s.isPalindrome("")
    if ex_2 != True:
        print("ERROR")
    pass