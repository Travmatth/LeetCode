"""
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = "1"
        for i in range(n)[1:]:
            old = string
            string = ""
            length = len(old)
            j = 0
            while True:
                count = 0
                orig = old[j]
                while j < length and old[j] == orig:
                    count += 1
                    j += 1
                string += str(count) + orig
                if j >= length:
                    break
        return string

         
if __name__ == "__main__":
    s = Solution()
    example_1 = s.countAndSay(1) #1
    example_2 = s.countAndSay(4) #1211
    example_3 = s.countAndSay(5) #111221
    example_4 = s.countAndSay(6) #312211
    pass