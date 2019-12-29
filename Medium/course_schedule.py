"""
There are a total of n courses you have to take,
labeled from 0 to n-1.
Some courses may have prerequisites, for example
to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]
Given the total number of courses and a list of
prerequisite pairs, is it possible for you to
finish all courses?
Note:
The input prerequisites is a graph represented by
a list of edges, not adjacency matrices. Read more
about how a graph is represented.
You may assume that there are no duplicate edges in
the input prerequisites.
"""

class Solution(object):
    def __init__(self):
        self.graph = []
        self.visited = []

    def dfs(self, node):
        # detected a cycle
        if self.visited[node] == True:
            return False
        # if visited
        elif self.visited[node] == False:
            return True
        # mark as visited
        self.visited[node] = True
        # visit all neighboring nodes
        for neighbor in self.graph[node]:
            # if a cycle exists
            if not self.dfs(neighbor):
                return False
        self.visited[node] = False
        return True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not len(prerequisites):
            return True
        # create graph
        self.graph = [[] for _ in range(numCourses)]
        # list graph edges
        for x, y in prerequisites:
            self.graph[x].append(y)
        # track visited status of each node
        self.visited = [None for _ in range(numCourses)]
        for i in range(numCourses):
            if not self.dfs(i):
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.canFinish(2, [[1,0]])
    if ex_0 != True:
        print("Error")
    # Explanation: There are a total of 2 courses to take. 
    # To take course 1 you should have finished course 0. So it is possible.
    ex_1 = s.canFinish(2, [[1,0],[0,1]])
    if ex_1 != False:
        print("Error")
    # Explanation: There are a total of 2 courses to take. 
    # To take course 1 you should have finished course 0, and to take course 0 you should
    # also have finished course 1. So it is impossible.
    pass