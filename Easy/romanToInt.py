class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        n = len(s)
        out = 0
        skip = False
        for i, char in enumerate(s):
            num = 0
            if skip:
                skip = False
                continue
            skip = True
            if i + 1 < n and char == "I" and s[i + 1] == "V":
                num = 4
            elif i + 1 < n and char == "I" and s[i + 1] == "X":
                num = 9
            elif i + 1 < n and char == "X" and s[i + 1] == "L":
                num = 40
            elif i + 1 < n and char == "X" and s[i + 1] == "C":
                num = 90
            elif i + 1 < n and char == "C" and s[i + 1] == "D":
                num = 400
            elif i + 1 < n and char == "C" and s[i + 1] == "M":
                num = 900
            else:
                num = lookup[char]
                skip = False
            out += num
        return out

if __name__ == '__main__':
    s = Solution()
    ex_0 = s.romanToInt("III") #3
    ex_1 = s.romanToInt("IV") #4
    ex_2 = s.romanToInt("IX") #9
    ex_3 = s.romanToInt("LVII") #58
    ex_4 = s.romanToInt("MCMXCIV") #1994
