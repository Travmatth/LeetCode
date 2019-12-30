"""
There are a total of n courses you have to take,
labeled from 0 to n-1.
Some courses may have prerequisites, for example
to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]
Given the total number of courses and a list of
prerequisite pairs, return the ordering of courses
you should take to finish all courses.
There may be multiple correct orders, you just need
to return one of them. If it is impossible to finish
all courses, return an empty array.
"""

class Solution(object):
    def dfs(self, node, graph, sorted_nodes, cycle):
        if cycle[node] == True:
            return False
        elif cycle[node] == None:
            cycle[node] = True
            for neighbor in graph[node]:
                if self.dfs(neighbor, graph, sorted_nodes, cycle) == False:
                    return False
            cycle[node] = False
            sorted_nodes.insert(0, node)
            

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = { i: [] for i in range(numCourses)}
        cycle, sorted_nodes  = [None for _ in range(numCourses)], []
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
        for node in graph:
            if self.dfs(node, graph, sorted_nodes, cycle) == False:
                return []
        return sorted_nodes

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.findOrder(2, [[1,0]])
    if ex_0 != [0,1]:
        print("error")
    # Explanation: There are a total of 2 courses to take.
    # To take course 1 you should have finished   
    # course 0. So the correct course order is [0,1] .
    ex_1 = s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    if ex_1 != [0,1,2,3] and ex_1 != [0,2,1,3]:
        print("error")
    # Explanation: There are a total of 4 courses to take.
    # To take course 3 you should have finished both courses 1 and 2.
    # Both courses 1 and 2 should be taken after you finished course 0. 
    # So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
    ex_2 = s.findOrder(2, [[1,0],[0,1]])
    if ex_2 != []:
        print("error")
    pass