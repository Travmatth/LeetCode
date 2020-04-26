#!/usr/local/bin/python3

"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the
square brackets is being repeated exactly k times. Note that k is guaranteed
to be a positive integer.

You may assume that the input string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. For example, there won't
be input like 3a or 2[4].
"""

class Solution(object):
  def decode(self, string, start, end):
    i = start
    if start >= end:
      return 0, ""
    while True:
      if i >= end:
        break
      elif string[i].isnumeric() or string[i] == "]":
        break
      i += 1
    segment = string[start:i] if i != start else ""
    if i >= end:
      return i, segment
    start = i
    while True:
      if i >= end:
        break
      if not string[i].isnumeric():
        break
      i += 1
    repeat = int(string[start:i]) if start != i else 1
    if string[i] == "[":
      j, next_segment = self.decode(string, i + 1, end)
      k, following_segment = self.decode(string, j, end)
      segment += (repeat * next_segment) 
      return k, segment + following_segment
    elif string[i] == "]":
      return i + 1, segment

  def decodeString(self, s):
      i, n = 0, len(s)
      _, string = self.decode(s, i, n)
      return string

if __name__ == "__main__":
  s = Solution()
  result = s.decodeString("")
  if result !=  "":
    print("error")
  result = s.decodeString("f")
  if result != "f":
    print("error")
  result = s.decodeString("0[f]")
  if result != "":
    print("error")
  result = s.decodeString("3[a]2[bc]")
  if result != "aaabcbc":
    print("error")
  result = s.decodeString("3[a2[c]]")
  if result != "accaccacc":
    print("error")
  result = s.decodeString("2[abc]3[cd]ef")
  if result != "abcabccdcdcdef":
    print("error")
  pass

