"""
Given two words (beginWord and endWord), and a dictionary's
word list, find the length of shortest transformation sequence
from beginWord to endWord, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note that beginWord is not a transformed word.
Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        n = len(beginWord)
        lookup = {}
        for word in wordList:
            for i in range(n):
                nxt = word[:i] + '_' + word[i + 1:]
                if nxt in lookup:
                    lookup[nxt].append(word)
                else:
                    lookup[nxt] = [word]
        queue, visited = [(beginWord, 1)], set(beginWord)
        while len(queue):
            cur, distance = queue.pop(0)
            for i in range(n):
                tmp = cur[:i] + '_' + cur[i + 1:]
                if tmp not in lookup:
                    continue
                for nxt in lookup[tmp]:
                    if nxt not in visited:
                        if nxt == endWord:
                            return distance + 1
                        queue.append((nxt, distance + 1))
                        visited.add(nxt)
        return 0

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    if ex_0 != 5:
        print("Error")
    # Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    ex_1 = s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])
    if ex_1 != 0:
        print("Error")
    # Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
    ex_1 = s.ladderLength("hot", "dog", ["hot","cog","dog","tot","hog","hop","pot","dot"])
    if ex_1 != 0:
        print("Error")
    pass