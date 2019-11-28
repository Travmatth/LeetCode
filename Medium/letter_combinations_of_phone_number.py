"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number
could represent.
A mapping of digit to letters (just like on the telephone
buttons) is given below. Note that 1 does not map to any letters.
Note:
Although the above answer is in lexicographical order,
your answer could be in any order you want.
"""

class Solution(object):
    def __init__(self):
        self.mapping = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"
        }

    def recurse(self, digits, ans):
        """
        :type digits: str
        :type ans: List[str]
        :rtype: List[str]
        """
        next = []
        if not digits or len(digits) == 0:
            return ans
        elif not ans:
            next = [letter for letter in self.mapping[digits[0]]]
        else:
            for base in ans:
                for letter in self.mapping[digits[0]]:
                    next.append(base + letter)
        return self.recurse(digits[1:], next)
    
    def iteration(self, digits):
        ans = []
        for digit in digits:
            if len(ans) == 0:
                ans = [letter for letter in self.mapping[digit]]
            else:
                next = []
                for base in ans:
                    for letter in self.mapping[digit]:
                        next.append(base + letter)
                ans = next
        return ans

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # return self.recurse(digits, [])
        return self.iteration(digits)

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.letterCombinations("23")
    # Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    ex_1 = s.letterCombinations("")
    pass